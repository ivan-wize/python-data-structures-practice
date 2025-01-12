class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
    # The matrix is traversed in four steps (in a loop):
    #   Left to Right (Top Row)
    #   Top to Bottom (Right Column)
    #   Right to Left (Bottom Row)
    #   Bottom to Top (Left Column)
    # After each step, the boundaries (top, bottom, left, right) are updated to move inward.

        # List to store the result
        result = []
        
        # Define the boundaries of the matrix
        top, bottom = 0, len(matrix) - 1  # Top and bottom rows
        left, right = 0, len(matrix[0]) - 1  # Left and right columns
        
        # Traverse the matrix in spiral order
        while top <= bottom and left <= right:
            # Traverse from left to right across the top row
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1  # Move the top boundary down
            
            # Traverse from top to bottom along the right column
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1  # Move the right boundary left
            
            # Check if there are still rows to traverse
            if top <= bottom:
                # Traverse from right to left across the bottom row
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1  # Move the bottom boundary up
            
            # Check if there are still columns to traverse
            if left <= right:
                # Traverse from bottom to top along the left column
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1  # Move the left boundary right
        
        return result

# Time Complexity: O(m * n)
#     Each element is visited exactly once.
# Space Complexity: O(1)
#     No additional data structures are used except the result list.

sol = Solution()

matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
print(sol.spiralOrder(matrix1))  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

matrix2 = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12]]
print(sol.spiralOrder(matrix2))  # Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

matrix3 = [[1, 2, 3, 4]]
print(sol.spiralOrder(matrix3))  # Output: [1, 2, 3, 4]

matrix4 = [[1], [2], [3], [4]]
print(sol.spiralOrder(matrix4))  # Output: [1, 2, 3, 4]

matrix5 = [[1]]
print(sol.spiralOrder(matrix5))  # Output: [1]
