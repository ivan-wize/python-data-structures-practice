# Problem: Device Heartbeat Monitor
# ---------------------------------
# In a production line, each test fixture/device sends a heartbeat every few seconds.
# If a device hasn’t sent a heartbeat within a timeout window, we consider it OFFLINE.
#
# Given:
#   - events: a list of (device_id: str, timestamp: int) heartbeats in any order
#   - current_time: int (seconds)
#   - timeout: int (seconds) — if last_heartbeat <= current_time - timeout => OFFLINE
#
# Return:
#   - offline_ids: List[str] of device IDs that are currently offline (sorted)
#   - age_by_id: Dict[str, int] mapping device_id -> seconds since its last heartbeat
#
# Constraints:
#   - 1 <= len(events) <= 2e5
#   - timestamps are UNIX-like seconds (monotonic per device but events list can be jumbled)
#   - A device appears at least once in events
#
# Examples:
#   events = [
#       ("fx-1", 100), ("fx-2", 120), ("fx-1", 130), ("fx-3", 90)
#   ]
#   current_time = 200
#   timeout = 60
#   last heartbeats => fx-1:130, fx-2:120, fx-3:90
#   ages at current_time 200 => fx-1:70, fx-2:80, fx-3:110
#   offline threshold = 200 - 60 = 140
#   OFFLINE: fx-1(130), fx-2(120), fx-3(90) -> all offline
#   Return (["fx-1","fx-2","fx-3"], {"fx-1":70,"fx-2":80,"fx-3":110})

from typing import List, Tuple, Dict

def heartbeat_monitor(events: List[Tuple[str, int]], current_time: int, timeout: int):
    # Track the most recent (max) timestamp seen for each device
    last_ts: Dict[str, int] = {}

    for dev, ts in events:
        # Keep the latest heartbeat only
        if dev not in last_ts or ts > last_ts[dev]:
            last_ts[dev] = ts

    # Compute "age" = seconds since last heartbeat
    age_by_id = {dev: current_time - ts for dev, ts in last_ts.items()}

    # Offline if last_ts <= current_time - timeout  <=>  age >= timeout
    offline_ids = sorted([dev for dev, age in age_by_id.items() if age >= timeout])

    return offline_ids, age_by_id


# ---- quick self-checks ----
if __name__ == "__main__":
    ev = [("fx-1", 100), ("fx-2", 120), ("fx-1", 130), ("fx-3", 90)]
    off, ages = heartbeat_monitor(ev, current_time=200, timeout=60)
    assert off == ["fx-1", "fx-2", "fx-3"]
    assert ages == {"fx-1": 70, "fx-2": 80, "fx-3": 110}

    ev2 = [("A", 10), ("B", 40), ("A", 50)]
    off2, ages2 = heartbeat_monitor(ev2, current_time=100, timeout=30)
    # last: A=50 (age=50), B=40 (age=60) => both offline
    assert off2 == ["A", "B"]
    assert ages2 == {"A": 50, "B": 60}
    print("All sample tests passed.")
