# You're building a test automation script to monitor battery temperature during stress testing. 
# The system records temperature readings every minute in Celsius.
# Write a Python function that:
#     Accepts a list of temperature readings.
#     Flags all the timestamps (i.e., index positions) where the temperature exceeds a critical threshold (e.g., 45°C).
#     Returns a list of those timestamp indices.

class Solution(object):
    def findTempBreaches(self, temps, threshold):
        """
        :type temps: List[float]      # Battery temperature readings in Celsius
        :type threshold: float        # Critical temperature limit
        :rtype: List[int]             # Indices where readings exceed threshold
        """

        # Store indices where temperature exceeds threshold
        breaches = []

        for i, temp in enumerate(temps):
            if temp > threshold:
                breaches.append(i)

        return breaches

# Time Complexity: O(n)
#     Where n is the number of temperature samples.
# Space Complexity: O(k)
#     Where k is the number of readings exceeding the threshold.

sol = Solution()

# Test Case 1: Mixed temperatures
temps = [34.5, 37.0, 41.2, 46.0, 44.9, 47.3]
threshold = 45.0
print(sol.findTempBreaches(temps, threshold))  # Expected: [3, 5]

# Test Case 2: No breaches
temps = [30.0, 35.0, 39.9]
print(sol.findTempBreaches(temps, 45.0))  # Expected: []

# Test Case 3: All breach
temps = [46.0, 48.5, 50.1]
print(sol.findTempBreaches(temps, 45.0))  # Expected: [0, 1, 2]

# Test Case 4: Edge values (equal to threshold)
temps = [45.0, 45.0, 44.9, 45.1]
print(sol.findTempBreaches(temps, 45.0))  # Expected: [3]

# Test Case 5: Empty list
temps = []
print(sol.findTempBreaches(temps, 45.0))  # Expected: []
