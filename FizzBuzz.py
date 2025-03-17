class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
    # If a number is divisible by both 3 and 5, it must be divisible by 15.
    # Numbers divisible by 3 are replaced with "Fizz".
    # Numbers divisible by 5 are replaced with "Buzz".
    # Other numbers are added to the result as their string representation.

        # Initialize an empty list to store the result
        result = []
        
        # Iterate from 1 to n
        for i in range(1, n + 1):
            # Check if the current number is divisible by both 3 and 5
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            # Check if the current number is divisible by 3
            elif i % 3 == 0:
                result.append("Fizz")
            # Check if the current number is divisible by 5
            elif i % 5 == 0:
                result.append("Buzz")
            # Otherwise, add the number as a string
            else:
                result.append(str(i))
        
        # Return the final list
        return result

# Time Complexity: O(n)
#     We iterate through all numbers from 1 to n once.
# Space Complexity: O(n)
#     The result list stores n strings.

sol = Solution()
print(sol.fizzBuzz(3))  # Output: ["1", "2", "Fizz"]
print(sol.fizzBuzz(5))  # Output: ["1", "2", "Fizz", "4", "Buzz"]
print(sol.fizzBuzz(15)) # Output: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
print(sol.fizzBuzz(1))  # Output: ["1"]
print(sol.fizzBuzz(20)) # Output: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz", "16", "17", "Fizz", "19", "Buzz"]
