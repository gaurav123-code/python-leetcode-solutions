"""
You are given an array prices where prices[i] is the price of a given stock 
on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing 
a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve 
any profit, return 0.
"""


class Solution(object):
    def maxProfit(self, prices):
        minimum_price = prices[0]   
        maximum_profit = 0          

        for current_price in prices:

            if current_price < minimum_price:
                minimum_price = current_price

            current_profit = current_price - minimum_price
            
            if current_profit > maximum_profit:
                maximum_profit = current_profit

        return maximum_profit

            


print(Solution().maxProfit([7,1,5,3,6,4]))
print(Solution().maxProfit([9,8,4,1]))