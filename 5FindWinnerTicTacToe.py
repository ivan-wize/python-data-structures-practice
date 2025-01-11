class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        # Initialize a 3x3 grid with empty strings
        grid = [[""] * 3 for _ in range(3)]
        
        # Fill the grid with the moves alternately for players A and B
        for i, (row, col) in enumerate(moves):
            grid[row][col] = "X" if i % 2 == 0 else "O"
        
        # Check all rows, columns, and diagonals for a winner
        def check_winner(player):
            # Check rows and columns
            for i in range(3):
                if all(grid[i][j] == player for j in range(3)) or \
                   all(grid[j][i] == player for j in range(3)):
                    return True
            # Check diagonals
            if all(grid[i][i] == player for i in range(3)) or \
               all(grid[i][2 - i] == player for i in range(3)):
                return True
            return False
        
        # Determine the winner
        if check_winner("X"):
            return "A"
        elif check_winner("O"):
            return "B"
        
        # If all moves have been made, and there's no winner, it's a draw
        if len(moves) == 9:
            return "Draw"
        
        # Otherwise, the game is still pending
        return "Pending"

# Explanation:
# Key Observations:
#     The game grid is a 3x3 matrix, which starts empty.
#     Players alternate turns:
#         Player A places X on even turns (0, 2, 4, ...).
#         Player B places O on odd turns (1, 3, 5, ...).
#     To determine the winner:
#         Check all rows, columns, and diagonals to see if they contain the same character (X or O).

# Time Complexity: O(9) (Constant, since the grid is fixed at 3x3).
#     Checking rows, columns, and diagonals involves at most 9 checks.
# Space Complexity: O(1) (No additional data structures other than the grid).
