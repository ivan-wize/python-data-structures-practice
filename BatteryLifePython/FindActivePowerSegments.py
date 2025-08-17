# You’re automating the analysis of battery test sessions. Each session is a list of power usage readings (in watts), one per minute.
# Write a Python function that:
#     Accepts a list of power readings from a test session.
#     Splits the session into continuous segments where power usage is above a given threshold (e.g., device is "active").
#     Returns a list of tuples, each representing a segment: (start_index, end_index), inclusive.

class Solution(object):
    def findActivePowerSegments(self, readings, threshold):
        """
        :type readings: List[float]     # Power usage per minute (watts)
        :type threshold: float          # Active usage threshold
        :rtype: List[Tuple[int, int]]   # List of (start, end) active segments
        """
        segments = []
        start = None

        for i, value in enumerate(readings):
            if value > threshold:
                if start is None:
                    start = i  # Start of a new active segment
            else:
                if start is not None:
                    segments.append((start, i - 1))
                    start = None 

        # If the last value is part of a segment, close it
        if start is not None:
            segments.append((start, len(readings) - 1))

        return segments

# Time Complexity: O(n)
#     Single pass through the list.
# Space Complexity: O(k)
#     Where k is the number of active segments.

sol = Solution()

# Test Case 1: Basic active segments
readings = [0.0, 0.0, 1.2, 1.3, 0.0, 2.5, 2.6, 0.0, 0.0]
print(sol.findActivePowerSegments(readings, 1.0))  # Expected: [(2, 3), (5, 6)]

# Test Case 2: All below threshold
readings = [0.1, 0.3, 0.0]
print(sol.findActivePowerSegments(readings, 1.0))  # Expected: []

# Test Case 3: One long active segment
readings = [1.2, 1.4, 1.6, 1.1]
print(sol.findActivePowerSegments(readings, 1.0))  # Expected: [(0, 3)]

# Test Case 4: Alternating spikes
readings = [0.0, 1.1, 0.0, 1.2, 0.0, 1.3]
print(sol.findActivePowerSegments(readings, 1.0))  # Expected: [(1, 1), (3, 3), (5, 5)]

# Test Case 5: Empty list
readings = []
print(sol.findActivePowerSegments(readings, 1.0))  # Expected: []
