class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Initialize left and right pointers 
        left = 0
        right = 1
        
        # Max profit to start is 0
        maxProfit = 0

        # While the left pointer is less than the lenght of prices
        while right < len(prices):
            # Verifies the price of the left pointer is than the price of the right pointer
            if prices[left] < prices[right]:
                # Calculates the profit 
                profit = prices[right] - prices[left]
                # Returns the max profit of maxProfit and profit, sets that value to maxProfit
                maxProfit = max(maxProfit, profit)
            else:
                # Left pointer increments to the right pointer
                left = right
            # Right pointer increments
            right +=1
        # We return the max profit after iterating through the array
        return maxProfit