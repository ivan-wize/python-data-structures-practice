class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Initialize a pointer to track the position of non-zero elements
        non_zero_index = 0
        
        # Iterate through the array
        for i in range(len(nums)):
            # If the current element is non-zero, swap it with the element at non_zero_index
            if nums[i] != 0:
                nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
                # Move the non_zero_index pointer forward
                non_zero_index += 1

# Explanation:
# Key Observations:

#     The problem requires:
#         All non-zero elements to be in their original relative order.
#         All zeros to be moved to the end.
#     Use a two-pointer approach to achieve the goal in one pass.

# Approach:
#     Pointer for Non-Zero Elements:
#         Use non_zero_index to track where the next non-zero element should be placed.

#     Iterate Through the Array:
#         For each non-zero element at index i:
#             Swap it with the element at non_zero_index.
#             Increment non_zero_index.
#     Result:
#         All non-zero elements are placed in their correct relative order.
#         Zeros are moved to the end.
