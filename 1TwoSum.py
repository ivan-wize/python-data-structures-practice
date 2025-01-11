class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]    # Input: A list of integers
        :type target: int        # Input: An integer representing the target sum
        :rtype: List[int]        # Output: A list containing the indices of the two numbers that add up to the target
        """
        # Initialize a dictionary to store numbers as keys and their indices as values
        # This will allow us to quickly check if the complement exists in constant time O(1)
        num_to_index = {}
        
        # Loop through each number in the list along with its index
        for i, num in enumerate(nums):
            # Calculate the complement that, when added to the current number, equals the target
            complement = target - num
            
            # Check if the complement is already in the dictionary
            # This means we've previously seen a number that, combined with the current number, adds up to the target
            if complement in num_to_index:
                # If complement is found, return the index of the complement and the current index
                # Since the problem guarantees exactly one solution, we can return immediately
                return [num_to_index[complement], i]
            
            # If complement is not found, store the current number and its index in the dictionary
            # This helps us track numbers we've seen so far and look them up quickly
            num_to_index[num] = i

# Explanation:
#     Hash Map Approach:
#         Use a dictionary (num_to_index) to store each number and its corresponding index as we iterate through the list.

#     Complement Check:
#         For each number, calculate the complement (i.e., target - num).
#         Check if the complement is already in the dictionary.
#             If yes, we’ve found the pair, so return their indices.
#             If no, add the current number and its index to the dictionary.

# Time Complexity: O(n), since we traverse the list only once.
# Space Complexity: O(n), for storing elements in the dictionary

sol = Solution()
print(sol.twoSum([2,7,11,15], 9))  # Output: [0,1]
print(sol.twoSum([3,2,4], 6))      # Output: [1,2]
print(sol.twoSum([3,3], 6))        # Output: [0,1]
print(sol.twoSum([1,5,3,8], 11))   # Output: [1,3]
