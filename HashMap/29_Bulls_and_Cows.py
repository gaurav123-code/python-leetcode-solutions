"""
You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a 
guess, you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong 
position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that 
both secret and guess may contain duplicate digits.
"""


from collections import Counter

class Solution(object):
    def getHint(self, secret, guess):
        bulls = 0
        secret_count = Counter()
        guess_count = Counter()

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_count[s] += 1
                guess_count[g] += 1

        cows = 0

        for digit in secret_count:
            cows += min(secret_count[digit], guess_count[digit])

        return str(bulls) + "A" + str(cows) + "B"
    
print(Solution().getHint("1807","7810"))