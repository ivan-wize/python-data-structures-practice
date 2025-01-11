class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            # Increment count if the least significant bit (LSB) is 1
            count += n & 1
            # Right shift the bits of n by 1 to process the next bit
            n = n >> 1
        return count

# Explanation:
# Key Observations:

#     A "set bit" is a bit with a value of 1.
#     Using bitwise operations, we can efficiently count the number of set bits in an integer.

# Time Complexity: O(k)
#     k is the number of bits in the integer (log(n) for base 2).
#     Each iteration processes one bit.

# Space Complexity: O(1)
#     No additional data structures are used.


# Optimized Approach (Brian Kernighan’s Algorithm):
# Instead of processing all bits, you can directly skip over unset bits (0) using the operation n = n & (n - 1). This operation removes the rightmost set bit from n.

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            n = n & (n - 1)  # Removes the rightmost set bit
            count += 1
        return count

# Why is it faster?
#     Each iteration removes a set bit, reducing the total number of iterations to the number of set bits (O(number of set bits)), rather than the total number of bits.

sol = Solution()

# Test case 1: Simple binary with a few set bits
print(sol.hammingWeight(11))  # Output: 3

# Test case 2: Power of 2
print(sol.hammingWeight(128))  # Output: 1

# Test case 3: Large number
print(sol.hammingWeight(2147483645))  # Output: 30

# Test case 4: All bits set (32-bit max value)
print(sol.hammingWeight(2**32 - 1))  # Output: 32
