class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]  # Input: Array of integers
        :type val: int         # Input: Integer value to remove
        :rtype: int            # Output: Number of elements not equal to val (k)
        """
        # Initialize a pointer to track the position of valid elements
        k = 0  # Points to the next position for a non-val element
        
        # Iterate through the array
        for i in range(len(nums)):
            # If the current element is not equal to val
            if nums[i] != val:
                # Place it at the position tracked by k
                nums[k] = nums[i]
                # Increment k to move to the next position
                k += 1
        
        # Return the count of elements that are not equal to val
        return k


sol = Solution()

# Test case 1
nums = [3, 2, 2, 3]
val = 3
k = sol.removeElement(nums, val)
print(k, nums[:k])  # Output: 2, [2, 2]

# Test case 2
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
k = sol.removeElement(nums, val)
print(k, nums[:k])  # Output: 5, [0, 1, 3, 0, 4]

# Test case 3
nums = []
val = 1
k = sol.removeElement(nums, val)
print(k, nums[:k])  # Output: 0, []

# Test case 4
nums = [1]
val = 1
k = sol.removeElement(nums, val)
print(k, nums[:k])  # Output: 0, []

# Test case 5
nums = [4, 5, 6]
val = 7
k = sol.removeElement(nums, val)
print(k, nums[:k])  # Output: 3, [4, 5, 6]


# Time Complexity: O(n)
#     Single pass through the array with n elements.

# Space Complexity: O(1)
#     In-place modification; no extra data structures used.