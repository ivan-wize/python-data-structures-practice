class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

    # Iterate Through the Grid:
    #   For each cell (r, c), check if it is a "1".
    #   If it is, it represents the start of a new island.
    # Mark the Island:
    #   Use a Depth-First Search (DFS) to visit all connected "1" cells and mark them as "0" (to avoid counting them again).
    # Count Islands:
    #   Each time you find a new "1" cell, increment the island count and start a DFS from that cell.
    # Edge Cases:
    #   If the grid is empty (grid = []), return 0.

        # If the grid is empty, there are no islands
        if not grid:
            return 0

        # Get the dimensions of the grid
        rows, cols = len(grid), len(grid[0])
        
        # Function to perform DFS to mark all connected lands as visited
        def dfs(r, c):
            # Check if the current cell is out of bounds or already visited
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return
            
            # Mark the current cell as visited by setting it to "0"
            grid[r][c] = "0"
            
            # Visit all 4 neighboring cells (up, down, left, right)
            dfs(r - 1, c)  # Up
            dfs(r + 1, c)  # Down
            dfs(r, c - 1)  # Left
            dfs(r, c + 1)  # Right
        
        # Initialize the number of islands
        num_islands = 0
        
        # Iterate over every cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If the cell is land ("1"), it's part of a new island
                if grid[r][c] == "1":
                    num_islands += 1  # Increment the island count
                    dfs(r, c)  # Use DFS to mark all connected land as visited
        
        return num_islands

    # Time Complexity: O(m * n)
    #   Each cell is visited once during the iteration.
    #   Each "1" cell is also visited during the DFS.
    # Space Complexity: O(m * n) (worst case for DFS recursion stack if the grid is filled with "1").

sol = Solution()

grid1 = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
print(sol.numIslands(grid1))  # Output: 1

grid2 = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
print(sol.numIslands(grid2))  # Output: 3

print(sol.numIslands([]))  # Output: 0

grid4 = [["1"]]
print(sol.numIslands(grid4))  # Output: 1
