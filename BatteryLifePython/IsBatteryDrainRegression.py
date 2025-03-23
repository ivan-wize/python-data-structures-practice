# You're testing a new software release on a mobile device. You collect hourly battery percentage readings during idle conditions for two builds:
#     previous_build: Battery percentages over 5 hours from an older stable version
#     new_build: Battery percentages over 5 hours from the current build under test
# Write a Python function that:
#     Checks whether the battery drain in the new build is worse than in the previous build.
#     Returns True if the new build has regressed (drains faster), otherwise False.
# Assume battery levels only go down or stay flat (never up).

class Solution(object):
    def isBatteryDrainRegression(self, previous_build, new_build):
        """
        :type previous_build: List[int]  # Battery levels for stable build
        :type new_build: List[int]       # Battery levels for new build
        :rtype: bool                     # True if new build drains faster
        """

        # Validate length
        if len(previous_build) != len(new_build):
            raise ValueError("Input arrays must have the same length.")

        # Compare total battery drain
        previous_drain = previous_build[0] - previous_build[-1]
        new_drain = new_build[0] - new_build[-1]

        # Return True if new build drains more
        return new_drain > previous_drain

# Time Complexity: O(1)
#     Only compares the first and last elements; constant time.
# Space Complexity: O(1)
#     Uses a few variables, no extra data structures.

# ---------------------
# ✅ Test Cases
# ---------------------
sol = Solution()

# Test Case 1: Regression exists
prev = [100, 98, 96, 95, 94]
new =  [100, 97, 94, 90, 87]
print(sol.isBatteryDrainRegression(prev, new))  # True

# Test Case 2: No regression
prev = [100, 98, 96, 94, 92]
new =  [100, 99, 98, 97, 96]
print(sol.isBatteryDrainRegression(prev, new))  # False

# Test Case 3: Equal drain
prev = [100, 97, 95]
new  = [100, 98, 95]
print(sol.isBatteryDrainRegression(prev, new))  # False

# Test Case 4: Invalid input (length mismatch)
try:
    sol.isBatteryDrainRegression([100, 98, 96], [100, 97])
except ValueError as e:
    print(e)  # Input arrays must have the same length.
