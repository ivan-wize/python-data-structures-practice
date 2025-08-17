# =============================================================
# 1) Parse & Summarize Test Logs
# Problem:
#   Given test log lines like:
#   "[t] SUITE:network TEST ping result:PASS"
#   Summarize counts of PASS/FAIL per suite.
# Example:
#   -> {'network': {'PASS': 1, 'FAIL': 1}, 'sensors': {'PASS': 1, 'FAIL': 0}}
# =============================================================
import re
from collections import defaultdict, OrderedDict
import heapq
import time
from typing import Callable, Type

LOG_RE = re.compile(r"SUITE\s*:\s*(?P<suite>\w+).*?result\s*:\s*(?P<res>PASS|FAIL)", re.IGNORECASE)

def summarize_results(lines: list[str]) -> dict[str, dict[str, int]]:
    out = defaultdict(lambda: {'PASS': 0, 'FAIL': 0})
    for ln in lines:
        m = LOG_RE.search(ln)              # extract suite + result
        if not m: continue                 # skip bad/malformed lines
        suite, res = m.group('suite'), m.group('res').upper()
        out[suite][res] += 1               # increment count
    return dict(out)