# =============================================================
# 6) Merge Overlapping Intervals
# Problem:
#   Merge intervals that overlap.
# Example: [[1,3],[2,6],[8,10]] -> [[1,6],[8,10]]
# =============================================================
def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda x: x[0])        # sort by start time
    out = []
    for s, e in intervals:
        if not out or s > out[-1][1]:         # no overlap
            out.append([s, e])
        else:
            out[-1][1] = max(out[-1][1], e)   # merge overlap
    return out
