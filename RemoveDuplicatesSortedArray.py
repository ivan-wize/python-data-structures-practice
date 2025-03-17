class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]  # Input: A sorted list of integers
        :rtype: int            # Output: Number of unique elements (k)
        """
        # Edge case: If the array is empty, return 0
        if not nums:
            return 0
        
        # Initialize a pointer 'k' to track the position of unique elements
        k = 1  # Starts at 1 because the first element is always unique
        
        # Loop through the array starting from the second element
        for i in range(1, len(nums)):
            # If the current element is different from the previous unique element
            if nums[i] != nums[k - 1]:
                # Move the unique element to the 'k' position
                nums[k] = nums[i]
                # Increment 'k' to point to the next position for a unique element
                k += 1
        
        # Return the count of unique elements
        return k

sol = Solution()
nums = [1, 1, 2]
k = sol.removeDuplicates(nums)
print(k, nums[:k])  # Output: 2, [1, 2]

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = sol.removeDuplicates(nums)
print(k, nums[:k])  # Output: 5, [0, 1, 2, 3, 4]

nums = []
k = sol.removeDuplicates(nums)
print(k, nums[:k])  # Output: 0, []

nums = [1]
k = sol.removeDuplicates(nums)
print(k, nums[:k])  # Output: 1, [1]

nums = [1, 1, 1, 1]
k = sol.removeDuplicates(nums)
print(k, nums[:k])  # Output: 1, [1]

#     Time Complexity: O(n)
#         Single pass through the array with n elements.

#     Space Complexity: O(1)
#         In-place modification; no extra data structures used.