class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]  # Input: List of stock prices
        :rtype: int              # Output: Maximum profit
        """

    # To maximize profit, you need to:
    #   Buy at the lowest price seen so far.
    # Sell at the highest price after buying.
    #   Use two variables:
    #     min_price: Tracks the lowest price encountered while iterating.
    #     max_profit: Tracks the maximum profit calculated so far.

        # Initialize variables
        min_price = float('inf')  # Track the minimum price seen so far # In Python, float('inf') represents infinity, a value that is larger than any other number
        max_profit = 0            # Track the maximum profit
        
        # Iterate through the prices
        for price in prices:
            # Update the minimum price if the current price is lower
            if price < min_price:
                min_price = price
            else:
                # Calculate profit if selling at the current price
                profit = price - min_price
                # Update the maximum profit if this profit is higher
                max_profit = max(max_profit, profit)
        
        return max_profit

# Time Complexity: O(n)
#     We iterate through the list of prices once, where n is the length of the list.
# Space Complexity: O(1)
#     We use only two variables (min_price and max_profit) for tracking.

sol = Solution()

prices = [7, 1, 5, 3, 6, 4]
print(sol.maxProfit(prices))  # Output: 5

prices = [7, 6, 4, 3, 1]
print(sol.maxProfit(prices))  # Output: 0

prices = [2, 4, 1]
print(sol.maxProfit(prices))  # Output: 2

prices = [1]
print(sol.maxProfit(prices))  # Output: 0

prices = [1, 2]
print(sol.maxProfit(prices))  # Output: 1
