# Problem: Factory Fixture Scheduler (Minimize Total Test Time)
# ------------------------------------------------------------
# You’re running a factory line that flashes firmware and runs a validation suite
# on many devices. You have K identical test fixtures (parallel stations). Each
# device i takes jobs[i] minutes to complete (flash + test). A fixture can work
# on only one device at a time, but as soon as it finishes, it can start the next.
#
# Goal:
#   Compute the minimum total time (makespan) to complete all devices if you
#   schedule them optimally across K fixtures.
#
# Input:
#   - jobs: List[int]  # durations in minutes (1 <= len(jobs) <= 1e5)
#   - k: int           # number of fixtures (1 <= k <= 1e5)
#
# Output:
#   - int: minimum total time to complete all jobs
#
# Notes:
#   - Fixtures are identical (same speed).
#   - You can assign jobs in any order.
#   - Large inputs require an efficient solution.
#
# Examples:
#   jobs = [5, 3, 7, 2], k = 2
#   Optimal schedule:
#     fixture A: 7 + 2 = 9
#     fixture B: 5 + 3 = 8
#   -> answer = 9
#
#   jobs = [10, 10, 3, 3, 3], k = 3
#   One optimal schedule:
#     f1: 10
#     f2: 10
#     f3: 3 + 3 + 3 = 9
#   -> answer = 10
#
#   Edge case:
#     k >= len(jobs) -> answer = max(jobs) (each job can get its own fixture)
#
# Follow-up (not required for core solution, great to discuss in interview):
#   1) If certain jobs must run before others (dependencies), how would you adapt?
#   2) If fixtures have different speeds, how does the approach change?
#   3) If you want balanced utilization per fixture, not just makespan, what metric?


import heapq

def min_total_time(jobs, k):
    """
    Greedy + min-heap (priority queue) of fixture loads.

    Idea:
      - Always assign the next job to the fixture that will be free the earliest.
      - Track each fixture's current load (total assigned time) in a min-heap.
      - After all jobs are assigned, the answer is the max load (the heap's max),
        but we can track it incrementally as we go.

    Time:  O(n log k)   (n = number of jobs)
    Space: O(k)
    """
    if not jobs:
        return 0
    if k <= 1:
        return sum(jobs)
    if k >= len(jobs):
        return max(jobs)

    # Heuristic: assign longer jobs first improves packing (LPT rule).
    jobs_sorted = sorted(jobs, reverse=True)

    # Initialize k fixtures with 0 load each.
    loads = [0] * k
    heapq.heapify(loads)

    current_makespan = 0
    for t in jobs_sorted:
        earliest = heapq.heappop(loads)   # fixture that frees up the earliest
        new_load = earliest + t           # assign this job to that fixture
        current_makespan = max(current_makespan, new_load)
        heapq.heappush(loads, new_load)

    return current_makespan


# ---- quick self-checks ----
if __name__ == "__main__":
    assert min_total_time([5,3,7,2], 2) == 9
    assert min_total_time([10,10,3,3,3], 3) == 10
    assert min_total_time([1,2,3], 5) == 3
    assert min_total_time([], 2) == 0
    assert min_total_time([4,4,4,4], 1) == 16
    print("All sample tests passed.")
