# ============================================
# Problem 1 — Reverse a String (Production-safe)
# --------------------------------------------
# Write a function that returns the reverse of a string.
# Treat the input as general text (may include Unicode, spaces, punctuation).
#
# Example:
#   reverse_string("Ops SWE 🚀") -> "🚀 EWS spO"
def reverse_string(s: str) -> str:
    # Python slices are Unicode-aware; this handles emojis and multi-byte codepoints.
    return s[::-1]


# ---- Tests for Problem 1 ----
print("P1:", reverse_string("Ops SWE 🚀"))           # "🚀 EWS spO"
print("P1:", reverse_string("apple"))                # "elppa"
print("P1:", reverse_string(""))                     # ""


# ============================================
# Problem 2 — Valid Palindrome (Ignore Non-Alnum)
# -----------------------------------------------
# Given a string, return True if it reads the same forward/backward
# considering only alphanumeric characters and ignoring case.
#
# Example:
#   is_palindrome("A man, a plan, a canal: Panama") -> True
def is_palindrome(s: str) -> bool:
    # Keep only alphanumeric chars; compare lowercased string to its reverse.
    filtered = [ch.lower() for ch in s if ch.isalnum()]
    return filtered == filtered[::-1]


# ---- Tests for Problem 2 ----
print("P2:", is_palindrome("A man, a plan, a canal: Panama"))  # True
print("P2:", is_palindrome("race a car"))                      # False
print("P2:", is_palindrome("No 'x' in Nixon"))                 # True


# ============================================
# Problem 3 — Fibonacci Number (Iterative, O(n))
# ----------------------------------------------
# Return the n-th Fibonacci number, where F0=0, F1=1.
# n can be up to 10^6 in stress tests, so avoid recursion.
#
# Example:
#   fibonacci(6) -> 8  (0,1,1,2,3,5,8)
def fibonacci(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b  # slide window forward
    return a


# ---- Tests for Problem 3 ----
print("P3:", fibonacci(0))   # 0
print("P3:", fibonacci(1))   # 1
print("P3:", fibonacci(10))  # 55


# ============================================
# Problem 4 — Factorial (Iterative, Big Int-safe)
# -----------------------------------------------
# Compute n! for non-negative integer n. Return 1 for n in {0,1}.
# Use an iterative approach to avoid recursion depth issues.
#
# Example:
#   factorial(5) -> 120
def factorial(n: int) -> int:
    if n < 2:
        return 1
    ans = 1
    for x in range(2, n + 1):
        ans *= x
    return ans


# ---- Tests for Problem 4 ----
print("P4:", factorial(0))   # 1
print("P4:", factorial(5))   # 120
print("P4:", factorial(10))  # 3628800


# ============================================
# Problem 5 — Maximum Subarray Sum (Kadane’s)
# -------------------------------------------
# Given an integer array, find the contiguous subarray with the largest sum.
#
# Example:
#   max_subarray([-2,1,-3,4,-1,2,1,-5,4]) -> 6  (subarray [4,-1,2,1])
def max_subarray(nums: list[int]) -> int:
    curr = best = nums[0]
    for x in nums[1:]:
        # Either start new at x or extend the existing window
        curr = max(x, curr + x)
        best = max(best, curr)
    return best


# ---- Tests for Problem 5 ----
print("P5:", max_subarray([-2,1,-3,4,-1,2,1,-5,4]))  # 6
print("P5:", max_subarray([1]))                       # 1
print("P5:", max_subarray([5,4,-1,7,8]))              # 23


# ============================================
# Problem 6 — Two Sum (Hash Map, O(n))
# ------------------------------------
# Given nums and target, return indices of the two numbers that add up to target.
# Assume exactly one solution; you may not use the same element twice.
#
# Example:
#   two_sum([2,7,11,15], 9) -> [0,1]
def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i
    return []  # defensive; per problem there’s always a solution


# ---- Tests for Problem 6 ----
print("P6:", two_sum([2,7,11,15], 9))          # [0,1]
print("P6:", two_sum([3,2,4], 6))              # [1,2]
print("P6:", two_sum([3,3], 6))                # [0,1]


# ============================================
# Problem 7 — Merge Two Sorted Lists (Two Pointers)
# -------------------------------------------------
# Merge two ascending lists into a single ascending list.
#
# Example:
#   merge_sorted_lists([1,3,5], [2,4,6]) -> [1,2,3,4,5,6]
def merge_sorted_lists(a: list[int], b: list[int]) -> list[int]:
    i = j = 0
    out: list[int] = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i]); i += 1
        else:
            out.append(b[j]); j += 1
    # append remaining tail (at most one of these has elements)
    out.extend(a[i:])
    out.extend(b[j:])
    return out


# ---- Tests for Problem 7 ----
print("P7:", merge_sorted_lists([1,3,5], [2,4,6]))       # [1,2,3,4,5,6]
print("P7:", merge_sorted_lists([], [0,1]))              # [0,1]
print("P7:", merge_sorted_lists([1,2,7], [3,4,5,6,8]))   # [1,2,3,4,5,6,7,8]


# ============================================
# Problem 8 — Valid Parentheses (Stack)
# -------------------------------------
# Given a string with only '()[]{}', return True if it’s valid:
# - Right bracket must match the most recent left of the same type.
#
# Example:
#   is_valid_parentheses("({[]})") -> True
#   is_valid_parentheses("([)]")   -> False
def is_valid_parentheses(s: str) -> bool:
    stack: list[str] = []
    match = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in match:
            top = stack.pop() if stack else '#'
            if match[ch] != top:
                return False
        else:
            stack.append(ch)
    return not stack


# ---- Tests for Problem 8 ----
print("P8:", is_valid_parentheses("({[]})"))  # True
print("P8:", is_valid_parentheses("([)]"))    # False
print("P8:", is_valid_parentheses("()[]{}"))  # True


# ============================================
# Problem 9 — BFS Traversal (Graph, Queue)
# ----------------------------------------
# Given an adjacency list graph and a start node, return BFS order.
#
# Example:
#   g = {0:[1,2], 1:[2], 2:[3], 3:[]}
#   bfs(g, 0) -> [0,1,2,3]
from collections import deque

def bfs(graph: dict[int, list[int]], start: int) -> list[int]:
    seen = set([start])
    q = deque([start])
    order: list[int] = []
    while q:
        node = q.popleft()
        order.append(node)
        for nei in graph.get(node, []):
            if nei not in seen:
                seen.add(nei)
                q.append(nei)
    return order


# ---- Tests for Problem 9 ----
g1 = {0:[1,2], 1:[2], 2:[3], 3:[]}
print("P9:", bfs(g1, 0))   # [0,1,2,3]
g2 = {1:[2,3], 2:[4], 3:[4], 4:[]}
print("P9:", bfs(g2, 1))   # [1,2,3,4]


# ============================================
# Problem 10 — DFS Cycle Detection (Directed Graph)
# -------------------------------------------------
# Given a directed graph, return True if it has a cycle, else False.
# (Useful for detecting cycles in job dependencies or build graphs.)
#
# Example:
#   g = {0:[1], 1:[2], 2:[0]} -> True  (cycle)
#   g = {0:[1], 1:[2], 2:[]}  -> False
def has_cycle_directed(graph: dict[int, list[int]]) -> bool:
    UNVIS, VISITING, DONE = 0, 1, 2
    state: dict[int, int] = {}

    # Build complete node set (keys + any referenced neighbors)
    nodes = set(graph.keys())
    for vs in graph.values():
        nodes.update(vs)
    for n in nodes:
        state.setdefault(n, UNVIS)

    def dfs(node: int) -> bool:
        st = state[node]
        if st == VISITING:   # back-edge → cycle
            return True
        if st == DONE:
            return False
        state[node] = VISITING
        for nei in graph.get(node, []):
            if dfs(nei):
                return True
        state[node] = DONE
        return False

    for n in nodes:
        if state[n] == UNVIS and dfs(n):
            return True
    return False


# ---- Tests for Problem 10 ----
g_cycle = {0:[1], 1:[2], 2:[0]}
g_acyc  = {0:[1], 1:[2], 2:[]}
print("P10:", has_cycle_directed(g_cycle))  # True
print("P10:", has_cycle_directed(g_acyc))   # False
