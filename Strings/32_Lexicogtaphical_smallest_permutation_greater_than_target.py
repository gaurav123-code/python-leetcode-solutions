from collections import Counter


class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        count = Counter(s)
        prefix = []

        # Try to match target as much as possible
        for i in range(len(target)):
            ch = target[i]

            if count[ch] > 0:
                prefix.append(ch)
                count[ch] -= 1
            else:
                break

        # Try to make the answer greater by changing
        # the current position or an earlier position.
        for i in range(len(prefix), -1, -1):

            if i < len(prefix):
                ch = prefix.pop()
                count[ch] += 1

            # Find the smallest available character
            # greater than target[i]
            if i < len(target):
                for c in range(ord(target[i]) + 1, ord('z') + 1):
                    candidate = chr(c)

                    if count[candidate] > 0:
                        count[candidate] -= 1

                        return (
                            ''.join(prefix)
                            + candidate
                            + ''.join(
                                c * count[c]
                                for c in sorted(count)
                            )
                        )

        return ""