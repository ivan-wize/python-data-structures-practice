# ============================================================
# 1) Factory Yield by Station (from CSV-like lines)
# Problem:
#   Each line looks like: "2025-08-16, station=Aging, sn=ABC123, result=PASS"
#   Return per-station pass rate (0.0–1.0). Ignore malformed lines.
# Example:
#   ["..., station=Aging, ..., result=PASS", "... FAIL", "... station=ICT ... PASS"]
#   -> {"Aging": 0.5, "ICT": 1.0}
# ============================================================
from __future__ import annotations
import re, time, random, heapq
from typing import Callable, Type

def compute_yield(lines: list[str]) -> dict[str, float]:
    counts: dict[str, list[int]] = {}  # station -> [pass_cnt, total]
    for ln in lines:
        # simple key=value grabs; robust to spaces
        m_station = re.search(r"station\s*=\s*([A-Za-z0-9_\-]+)", ln)
        m_result  = re.search(r"result\s*=\s*(PASS|FAIL)", ln, re.IGNORECASE)
        if not (m_station and m_result):
            continue  # skip malformed
        st = m_station.group(1)
        res = m_result.group(1).upper()
        counts.setdefault(st, [0,0])
        counts[st][1] += 1
        counts[st][0] += 1 if res == "PASS" else 0
    # compute pass rate; avoid div-by-zero (though totals >0 if present)
    return {st: (p/t if t else 0.0) for st,(p,t) in counts.items()}


# ============================================================
# 2) Flaky Test Detector
# Problem:
#   Given recent outcomes ["PASS","FAIL",...], return True if
#   failure rate in last `window` runs > threshold AND we saw both PASS and FAIL.
# Example:
#   is_flaky(["PASS","PASS","FAIL","PASS"], window=4, threshold=0.2) -> False
# ============================================================
def is_flaky(outcomes: list[str], window: int = 10, threshold: float = 0.2) -> bool:
    recent = [s.upper() for s in outcomes[-window:]]
    if not recent:
        return False
    fails = sum(1 for s in recent if s == "FAIL")
    passes = sum(1 for s in recent if s == "PASS")
    if fails == 0 or passes == 0:  # need both to be "flaky", otherwise it's just failing/passing
        return False
    rate = fails / len(recent)
    return rate > threshold


# ============================================================
# 3) UART Key=Value Line Parser
# Problem:
#   Parse lines like "ts=1692213001 level=ERROR code=E42 msg=overcurrent"
#   Return list of dicts with typed fields; require at least ts and level.
# Example:
#   -> [{"ts":1,"level":"INFO","code":"OK","msg":"ready"}, ...]
# ============================================================
def parse_uart(lines: list[str]) -> list[dict]:
    out: list[dict] = []
    for ln in lines:
        entry: dict = {}
        ok = True
        for token in ln.strip().split():
            if "=" not in token:
                continue
            k, v = token.split("=", 1)
            # try int for ts; else keep string
            if k == "ts":
                try:
                    entry[k] = int(v)
                except ValueError:
                    ok = False
                    break
            else:
                entry[k] = v
        if ok and "ts" in entry and "level" in entry:
            out.append(entry)
    return out


# ============================================================
# 4) Minimal JSON “Schema” Validator
# Problem:
#   schema: {"temp":{"type":float,"required":True}, "id":{"type":str,"required":True}}
#   Validate required fields and types (float accepts int). Ignore extra fields.
#   Return (ok, errors[]).
# Example:
#   -> (True, [])
# ============================================================
def validate_json(obj: dict, schema: dict) -> tuple[bool, list[str]]:
    errors: list[str] = []
    for field, rules in schema.items():
        req = bool(rules.get("required", False))
        typ = rules.get("type", object)
        if req and field not in obj:
            errors.append(f"missing:{field}")
            continue
        if field in obj:
            val = obj[field]
            # allow int where float is expected
            if typ is float:
                if not isinstance(val, (int, float)):
                    errors.append(f"type:{field} expected float got {type(val).__name__}")
            else:
                if not isinstance(val, typ):
                    errors.append(f"type:{field} expected {getattr(typ,'__name__',typ)} got {type(val).__name__}")
    return (len(errors) == 0, errors)


# ============================================================
# 5) Rolling Outlier Filter (Median/MAD)
# Problem:
#   For each value, use median & MAD of last k values; flag if modified z-score > z.
#   Handle small windows and MAD==0 (do not flag unless deviation policy changed).
# Example:
#   flag_outliers([10,10,10,10,100,10]) -> [F,F,F,F,T,F]
# ============================================================
def flag_outliers(values: list[float], k: int = 5, z: float = 3.5) -> list[bool]:
    def median(nums: list[float]) -> float:
        s = sorted(nums)
        n = len(s)
        mid = n // 2
        return (s[mid] if n % 2 else (s[mid-1] + s[mid]) / 2.0)
    flags: list[bool] = []
    for i, x in enumerate(values):
        window = values[max(0, i - k + 1): i + 1]
        med = median(window)
        devs = [abs(v - med) for v in window]
        mad = median(devs)
        if mad == 0:
            flags.append(False)  # flat window; treat as not outlier
            continue
        mz = abs(x - med) / (1.4826 * mad)  # 1.4826 ~ scaling to stddev for normal
        flags.append(mz > z)
    return flags


# ============================================================
# 6) Timestamp Join with Tolerance
# Problem:
#   a,b are sorted [(ts_ms, val)]. For each a, find closest b within tol_ms.
#   Output matched tuples; skip if no b within tolerance.
# Example:
#   a=[(1000,1.0),(1100,1.2)], b=[(1045,0.9)], tol=60 -> [(1000,1.0,0.9)]
# ============================================================
def join_by_time(a: list[tuple[int,float]], b: list[tuple[int,float]], tol_ms: int = 50) -> list[tuple[int,float,float]]:
    out: list[tuple[int,float,float]] = []
    j = 0
    nb = len(b)
    for ts_a, va in a:
        # advance j while b[j] is definitely too old
        while j < nb and b[j][0] < ts_a - tol_ms:
            j += 1
        candidates = []
        if j < nb: candidates.append(b[j])
        if j - 1 >= 0: candidates.append(b[j-1])
        # pick the closest within tolerance
        best = None
        best_dt = None
        for ts_b, vb in candidates:
            dt = abs(ts_b - ts_a)
            if dt <= tol_ms and (best_dt is None or dt < best_dt):
                best, best_dt = (ts_a, va, vb), dt
        if best:
            out.append(best)
    return out


# ============================================================
# 7) Simple Retry with Jitter & Max Elapsed
# Problem:
#   Call fn() up to `attempts` with exponential backoff (base*2^(i-1)) + jitter [0,jitter].
#   Stop if total elapsed exceeds max_elapsed. Retry only on `exc` (default Exception).
# ============================================================
def call_with_retry(
    fn: Callable[[], object],
    attempts: int = 3,
    base: float = 0.1,
    jitter: float = 0.05,
    max_elapsed: float = 1.0,
    exc: Type[BaseException] = Exception,
    _sleep: Callable[[float], None] = time.sleep,
    _monotonic: Callable[[], float] = time.monotonic,
):
    start = _monotonic()
    last_err = None
    for i in range(1, attempts + 1):
        try:
            return fn()  # try call
        except exc as e:
            last_err = e
            if i == attempts:
                break
            # compute next delay; cap to remaining budget
            delay = base * (2 ** (i - 1)) + random.uniform(0, max(0.0, jitter))
            elapsed = _monotonic() - start
            remain = max_elapsed - elapsed
            if remain <= 0:
                break
            _sleep(min(delay, remain))
    # out of attempts or time
    raise last_err if last_err else RuntimeError("call_with_retry: no attempts made")


# ============================================================
# 8) Test Shard Assigner by Duration (LPT)
# Problem:
#   Distribute tests across k shards to balance total duration using greedy LPT.
# Example:
#   {"A":9,"B":8,"C":3,"D":2}, k=2 -> [["A","C"], ["B","D"]]
# ============================================================
def assign_shards(test_durations: dict[str,int], k: int) -> list[list[str]]:
    # min-heap of (total_duration, shard_index)
    shards = [(0, i) for i in range(k)]
    heapq.heapify(shards)
    result: list[list[str]] = [[] for _ in range(k)]
    # sort tests by duration desc
    for name, dur in sorted(test_durations.items(), key=lambda kv: kv[1], reverse=True):
        total, idx = heapq.heappop(shards)      # shard with smallest load
        result[idx].append(name)
        heapq.heappush(shards, (total + dur, idx))
    return result


# ============================================================
# 9) Latest Artifact Picker (SemVer + Date)
# Problem:
#   Pick the latest file by semantic version; tie-break by date (YYYYMMDD).
#   Filenames like "controller_v2.3.1_20250815.hex". Return None if none parse.
# Example:
#   -> "controller_v2.4.0_20250816.hex"
# ============================================================
_SEM_RE = re.compile(r"v(\d+)\.(\d+)\.(\d+)_([0-9]{8})", re.IGNORECASE)

def pick_latest(files: list[str]) -> str | None:
    best = None
    best_key = None  # (major,minor,patch, date_int)
    for f in files:
        m = _SEM_RE.search(f)
        if not m:
            continue
        maj, minr, pat, date = int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))
        key = (maj, minr, pat, date)
        if best_key is None or key > best_key:
            best, best_key = f, key
    return best


# ============================================================
# 10) Canary Decision from Metrics
# Problem:
#   metrics: {"error_rate":0.012, "p95_ms":210, "cpu":0.62}
#   thresholds: {"error_rate":0.01, "p95_ms":250, "cpu":0.8}
#   Return "promote" if all <= thresholds; "rollback" if any > 120% of threshold;
#   else "hold". Missing metric -> "hold".
# Example:
#   -> "hold" (small err_rate miss), "promote", or "rollback" for big miss
# ============================================================
def canary_decision(metrics: dict, thresholds: dict) -> str:
    # missing metric -> conservative hold
    for k in thresholds:
        if k not in metrics:
            return "hold"
    big_miss = any(metrics[k] > 1.2 * thresholds[k] for k in thresholds)
    if big_miss:
        return "rollback"
    all_ok = all(metrics[k] <= thresholds[k] for k in thresholds)
    if all_ok:
        return "promote"
    return "hold"
