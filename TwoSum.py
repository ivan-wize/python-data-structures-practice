class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]    # Input: A list of integers
        :type target: int        # Input: An integer representing the target sum
        :rtype: List[int]        # Output: A list containing the indices of the two numbers that add up to the target
        """
    # Hash Map Approach:
    #   Use a dictionary (num_to_index) to store each number and its corresponding index as we iterate through the list.
    # Complement Check:
    #   For each number, calculate the complement (i.e., target - num).
    #   Check if the complement is already in the dictionary.
    #     If yes, we’ve found the pair, so return their indices.
    #     If no, add the current number and its index to the dictionary.

        # Initialize a dictionary to store numbers as keys and their indices as values
        num_to_index = {}
        
        # Loop through each number in the list along with its index
        for i, num in enumerate(nums): # enumerate is useful for obtaining an indexed list: (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
            # Calculate the complement that, when added to the current number, equals the target
            complement = target - num
            
            # Check if the complement is already in the dictionary
            if complement in num_to_index:
                # If complement is found, return the index of the complement and the current index
                return [num_to_index[complement], i]
            
            # If complement is not found, store the current number and its index in the dictionary
            num_to_index[num] = i

# Time Complexity: O(n), since we traverse the list only once.
# Space Complexity: O(n), for storing elements in the dictionary

sol = Solution()
print(sol.twoSum([2,7,11,15], 9))  # Output: [0,1]
print(sol.twoSum([3,2,4], 6))      # Output: [1,2]
print(sol.twoSum([3,3], 6))        # Output: [0,1]
print(sol.twoSum([1,5,3,8], 11))   # Output: [1,3]
