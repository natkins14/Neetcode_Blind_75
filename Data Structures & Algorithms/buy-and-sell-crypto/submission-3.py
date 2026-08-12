class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Set max profit to 0
        maxProfit = 0

        # Set minimum buy to first price
        minBuy = prices[0]

        # Iterate through prices
        for x in prices:
            # Set max profit to the max of current max profit and current value minus minimum value
            maxProfit = max(maxProfit, x - minBuy)
            # Set minimum value to the minimum of current number and minimum value
            minBuy = min(minBuy, x)
        # Return the max profit 
        return maxProfit