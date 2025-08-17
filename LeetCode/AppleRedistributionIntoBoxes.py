class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        # Calculate the total number of apples
        total_apples = sum(apple)
        
        # Sort the capacity array in descending order
        capacity.sort(reverse=True)
        
        # Initialize variables to track the number of boxes used and apples packed
        boxes_used = 0
        apples_packed = 0
        
        # Iterate over the sorted capacity array
        for cap in capacity:
            # Use the current box
            apples_packed += cap
            boxes_used += 1
            
            # Check if we have packed all apples
            if apples_packed >= total_apples:
                return boxes_used
        
        # Return the number of boxes used
        return boxes_used

# Explanation:
# Key Observations:
#     To minimize the number of boxes used, we should prioritize boxes with the largest capacity.
#     By sorting the capacity array in descending order, we ensure that we use the largest boxes first.

# Approach:
#     Calculate Total Apples:
#         Compute the sum of the apple array to determine the total number of apples that need to be packed.

#     Sort Capacities:
#         Sort the capacity array in descending order to use the largest boxes first.

#     Pack Apples:
#         Iterate through the sorted capacity array and add the capacity of each box to a running total (apples_packed).
#         Keep track of the number of boxes used.
#         Stop as soon as apples_packed is greater than or equal to total_apples.

#     Return Result:
#         Return the number of boxes used.

# Time Complexity:
#     Sorting capacity takes O(m log m), where m is the length of the capacity array.
#     Iterating through capacity takes O(m).
#     Total: O(m log m).

# Space Complexity:
#     O(1) (no additional data structures are used apart from variables).

sol = Solution()

# Test case 1
print(sol.minimumBoxes([1, 3, 2], [4, 3, 1, 5, 2]))  # Output: 2

# Test case 2
print(sol.minimumBoxes([5, 5, 5], [2, 4, 2, 7]))  # Output: 4

# Test case 3
print(sol.minimumBoxes([10, 20], [30, 10, 10]))  # Output: 2

# Test case 4
print(sol.minimumBoxes([1], [1]))  # Output: 1

# Test case 5
print(sol.minimumBoxes([3, 3, 3], [9, 1, 1]))  # Output: 1
