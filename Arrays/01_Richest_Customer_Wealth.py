"""
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money 
the ith customer has in the jth bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. 
The richest customer is the customer that has the maximum wealth.

"""


class Solution:
    def maximumWealth(self, accounts):
        max_wealth = 0

        for customer in accounts:
            wealth = sum(customer)

            if wealth > max_wealth:
                max_wealth = wealth

        return max_wealth
    
