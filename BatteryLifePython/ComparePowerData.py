# You're working on a team that validates battery performance on a mobile device. You are given two arrays of power data:
#     measured_data: captured from a DC power analyzer connected to the battery during a test run.
#     expected_data: the "correct" or reference power data generated from a simulation or a known-good run.
# Each array contains floating-point numbers representing power usage in watts, sampled once per second.
# Write a Python function that:
#     Compares measured_data to expected_data.
#     Flags all timestamps (index positions) where the absolute difference between the two exceeds a given threshold (e.g. 0.5W).
#     Returns a list of these timestamp indices along with the delta (measured - expected) at that time.

class Solution(object):
    def comparePowerData(self, measured_data, expected_data, threshold):
        """
        :type measured_data: List[float]  # Actual power data from DC analyzer
        :type expected_data: List[float]  # Reference or simulated expected values
        :type threshold: float            # Threshold for flagging significant differences
        :rtype: List[Tuple[int, float]]   # List of (index, delta) where |delta| >= threshold
        """

        # Validate input lengths to ensure arrays are aligned
        if len(measured_data) != len(expected_data):
            raise ValueError("Input arrays must be of the same length.")

        differences = []  # Store indices and deltas where difference exceeds threshold

        # Iterate over both arrays using zip to pair measured and expected values
        for i, (measured, expected) in enumerate(zip(measured_data, expected_data)):
            delta = measured - expected  # Compute difference
            if abs(delta) >= threshold:  # Check if it exceeds the threshold
                differences.append((i, round(delta, 3)))  # Round for cleaner output

        return differences

# Time Complexity: O(n)
#     We iterate through the input lists once, where n is the number of samples.
# Space Complexity: O(k)
#     Where k is the number of differences exceeding the threshold.
#     In the worst case, k = n (if every value differs significantly).

sol = Solution()

# Test Case 1: Basic comparison with two differences
measured_data = [2.1, 3.5, 5.0, 4.9, 6.2]
expected_data = [2.0, 3.0, 5.1, 4.9, 5.5]
threshold = 0.5
print(sol.comparePowerData(measured_data, expected_data, threshold))
# Expected Output: [(1, 0.5), (4, 0.7)]

# Test Case 2: No differences above threshold
measured_data = [1.0, 2.1, 3.0]
expected_data = [1.0, 2.0, 3.0]
threshold = 0.2
print(sol.comparePowerData(measured_data, expected_data, threshold))
# Expected Output: []

# Test Case 3: All values differ beyond threshold
measured_data = [4.0, 4.0, 4.0]
expected_data = [2.0, 1.5, 3.2]
threshold = 0.5
print(sol.comparePowerData(measured_data, expected_data, threshold))
# Expected Output: [(0, 2.0), (1, 2.5), (2, 0.8)]

# Test Case 4: Edge case - identical arrays
measured_data = [5.0, 5.0, 5.0]
expected_data = [5.0, 5.0, 5.0]
threshold = 0.1
print(sol.comparePowerData(measured_data, expected_data, threshold))
# Expected Output: []

# Test Case 5: Edge case - mismatched lengths
try:
    measured_data = [1.0, 2.0]
    expected_data = [1.0]
    threshold = 0.1
    print(sol.comparePowerData(measured_data, expected_data, threshold))
except ValueError as e:
    print(e)


# Expected Output: "Input arrays must be of the same length."

# from typing import List, Tuple

# def compare_power_data(measured_data: List[float], expected_data: List[float], threshold: float) -> List[Tuple[int, float]]:
#     if len(measured_data) != len(expected_data):
#         raise ValueError("Input arrays must be of the same length.")

#     differences = []
#     for i, (measured, expected) in enumerate(zip(measured_data, expected_data)):
#         delta = measured - expected
#         if abs(delta) >= threshold:
#             differences.append((i, round(delta, 3)))

#     return differences
