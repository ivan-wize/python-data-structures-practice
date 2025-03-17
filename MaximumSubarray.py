# Here's the solution for finding the subarray with the largest sum using Kadane's Algorithm (O(n) time complexity)
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    # A subarray is a contiguous portion of an array.
    # To maximize the sum of a subarray:
    #   Add the current element to the running sum (current_sum).
    #   If adding the current element makes the sum worse, start a new subarray from the current element.

        # Initialize the maximum sum as the first element
        max_sum = nums[0]
        # Initialize the current sum as the first element
        current_sum = nums[0]
        
        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # Update the current sum by either adding the current number to the
            # previous sum or starting fresh with the current number
            current_sum = max(nums[i], current_sum + nums[i])
            
            # Update the maximum sum if the current sum is larger
            max_sum = max(max_sum, current_sum)
        
        return max_sum

# Time Complexity: O(n)
#     We iterate through the array once.
# Space Complexity: O(1)
#     We use only a few variables for tracking the current sum and maximum sum.

sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
print(sol.maxSubArray([1]))  # Output: 1
print(sol.maxSubArray([5,4,-1,7,8]))  # Output: 23
print(sol.maxSubArray([-1]))  # Output: -1
print(sol.maxSubArray([-2, -3, -1, -5]))  # Output: -1
