"""
You are given a string num which represents a positive integer, and an integer t.

A number is called zero-free if none of its digits are 0.

Return a string representing the smallest zero-free number greater than or equal to num such that the product of 
its digits is divisible by t. If no such number exists, return "-1".
"""


from functools import lru_cache


class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Factorize t into 2, 3, 5, 7
        need = [0, 0, 0, 0]
        primes = [2, 3, 5, 7]

        for i, p in enumerate(primes):
            while t % p == 0:
                need[i] += 1
                t //= p

        # If t has any other prime factor
        if t != 1:
            return "-1"

        # Digit -> contribution of (2, 3, 5, 7)
        contribution = [
            (0, 0, 0, 0),  # 0
            (0, 0, 0, 0),  # 1
            (1, 0, 0, 0),  # 2
            (0, 1, 0, 0),  # 3
            (2, 0, 0, 0),  # 4
            (0, 0, 1, 0),  # 5
            (1, 1, 0, 0),  # 6
            (0, 0, 0, 1),  # 7
            (3, 0, 0, 0),  # 8
            (0, 2, 0, 0),  # 9
        ]

        original_length = len(num)

        # Try numbers with length len(num), len(num)+1, ...
        for length in range(original_length, original_length + 100):
            if length == original_length:
                lower = num
            else:
                lower = "1" * length

            @lru_cache(None)
            def can_build(pos, a, b, c, d, tight):
                if pos == length:
                    return a == b == c == d == 0

                remaining = length - pos

                # Maximum contribution possible from remaining digits
                if a > 3 * remaining:
                    return False
                if b > 2 * remaining:
                    return False
                if c > remaining:
                    return False
                if d > remaining:
                    return False

                start = int(lower[pos]) if tight else 1

                for digit in range(start, 10):
                    if digit == 0:
                        continue

                    x, y, z, w = contribution[digit]

                    next_tight = tight and digit == int(lower[pos])

                    if can_build(
                        pos + 1,
                        max(0, a - x),
                        max(0, b - y),
                        max(0, c - z),
                        max(0, d - w),
                        next_tight
                    ):
                        return True

                return False

            # If a solution exists, construct the smallest one
            if can_build(0, *need, True):

                answer = []
                pos = 0
                a, b, c, d = need
                tight = True

                while pos < length:
                    start = int(lower[pos]) if tight else 1

                    for digit in range(start, 10):
                        if digit == 0:
                            continue

                        x, y, z, w = contribution[digit]
                        next_tight = tight and digit == int(lower[pos])

                        if can_build(
                            pos + 1,
                            max(0, a - x),
                            max(0, b - y),
                            max(0, c - z),
                            max(0, d - w),
                            next_tight
                        ):
                            answer.append(str(digit))
                            a = max(0, a - x)
                            b = max(0, b - y)
                            c = max(0, c - z)
                            d = max(0, d - w)
                            tight = next_tight
                            break

                    pos += 1

                return "".join(answer)

        return "-1"
    
print(Solution().smallestNumber("1234",256))