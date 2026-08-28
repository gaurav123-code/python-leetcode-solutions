class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        half = n // 2

        # Count characters
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        # More than one odd frequency -> no palindrome possible
        if sum(x % 2 for x in freq) > 1:
            return ""

        # Middle character for odd length
        middle = ""

        for i in range(26):
            if freq[i] % 2:
                middle = chr(ord('a') + i)
            freq[i] //= 2

        ans = [""] * n

        # Match target from left to right
        pos = 0

        while pos < half:
            c = ord(target[pos]) - ord('a')

            if freq[c] == 0:
                break

            ans[pos] = target[pos]
            freq[c] -= 1
            pos += 1

        def make_palindrome():
            if middle:
                ans[half] = middle

            for i in range(half):
                ans[n - 1 - i] = ans[i]

        # Important:
        # First check whether matching the entire left half
        # already gives a palindrome > target.
        if pos == half:
            make_palindrome()

            result = ''.join(ans)

            if result > target:
                return result

        # Now make the answer larger.
        while True:

            if pos < half:

                # We need the smallest available character
                # greater than target[pos].
                c = ord(target[pos]) - ord('a') + 1

                while c < 26 and freq[c] == 0:
                    c += 1

                if c < 26:
                    ans[pos] = chr(ord('a') + c)
                    freq[c] -= 1

                    # Fill remaining positions with the
                    # smallest possible characters.
                    idx = pos + 1

                    for ch in range(26):
                        for _ in range(freq[ch]):
                            ans[idx] = chr(ord('a') + ch)
                            idx += 1

                    make_palindrome()

                    return ''.join(ans)

            # We couldn't make target[pos] larger.
            # Move backward and try to increase an earlier position.
            if pos == 0:
                return ""

            pos -= 1

            c = ord(target[pos]) - ord('a')
            freq[c] += 1