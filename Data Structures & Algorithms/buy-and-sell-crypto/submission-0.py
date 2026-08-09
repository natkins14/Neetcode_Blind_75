class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0

        min_price = prices[0]

        for x in prices:

            if x < min_price:
                min_price = x

            profit = x - min_price

            if profit > max_profit:

                max_profit = profit

        return max_profit
            


                