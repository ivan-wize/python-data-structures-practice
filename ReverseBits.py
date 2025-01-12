class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        """
        Reverse the bits of a 32-bit unsigned integer.
        :type n: int
        :rtype: int
        """
        # Initialize the result to 0
        result = 0
        
        # Iterate over 32 bits
        for i in range(32):
            # Extract the least significant bit of n (n & 1)
            bit = n & 1
            
            # Left shift the result to make room for the new bit
            result = (result << 1) | bit
            
            # Right shift n to process the next bit
            n = n >> 1
        
        return result
    
sol = Solution()
print(sol.reverseBits(43261596))  # Output: 964176192
print(sol.reverseBits(4294967293))  # Output: 3221225471
print(sol.reverseBits(0))  # Output: 0
print(sol.reverseBits(1))  # Output: 2147483648
    
    # Explanation:

    # Input Representation:
    #     The input n is treated as a 32-bit unsigned integer.
    #     We process each bit, starting from the least significant bit (LSB).

    # Reversal Logic:
    #     Initialize result = 0.
    #     For each bit in n:
    #         Extract the LSB using n & 1.
    #         Left shift result to make space for the next bit.
    #         Append the extracted bit to result using the bitwise OR (|).
    #         Right shift n to move to the next bit.

    # Output Representation:
    #     Return the result, which is the reversed 32-bit integer.

# Time Complexity: O(32)
#     Fixed loop of 32 iterations regardless of input size.

# Space Complexity: O(1)
#     No additional space is used; operations are performed in-place.

