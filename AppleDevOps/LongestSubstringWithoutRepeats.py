# =============================================================
# 5) Longest Substring Without Repeats
# Problem:
#   Find length of longest substring with unique chars.
# Example: "abcabcbb" -> 3
# =============================================================
def length_of_longest_substring(s: str) -> int:
    last, left, best = {}, 0, 0
    for right, ch in enumerate(s):
        if ch in last and last[ch] >= left:   # duplicate found
            left = last[ch] + 1               # move left past duplicate
        last[ch] = right                      # update last seen index
        best = max(best, right - left + 1)    # update max window
    return best
