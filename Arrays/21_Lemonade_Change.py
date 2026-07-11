"""
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue 
to buy from you and order one at a time (in the order specified by bills). 
Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. 
You must provide the correct change to each customer so that the net 
transaction is that the customer pays $5.

Note that you do not have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays, 
return true if you can provide every customer with the correct change, or false otherwise.
"""

class Solution(object):
    def lemonadeChange(self, bills):

        five_rupee = 0
        ten_rupee = 0

        for bill in bills:

            if bill == 5:
                five_rupee += 1

            elif bill == 10:

                if five_rupee > 0:
                    five_rupee -= 1
                    ten_rupee += 1
                else:
                    return False

            else:

                if ten_rupee > 0 and five_rupee > 0:
                    ten_rupee -= 1
                    five_rupee -= 1

                elif five_rupee >= 3:
                    five_rupee -= 3

                else:
                    return False

        return True


print(Solution().lemonadeChange([5, 5, 5, 10, 10, 20]))