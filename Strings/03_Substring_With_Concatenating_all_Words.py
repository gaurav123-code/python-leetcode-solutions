"""
You are given a string s and an array of strings words. All the strings of words are of the same 
length.

A concatenated string is a string that exactly contains all the strings of any permutation 
of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", 
and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because 
it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. 

You can return the answer in any order.
"""

from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        total_words = len(words)
        total_len = word_len * total_words

        word_count = Counter(words)
        ans = []

        for i in range(word_len):
            left = i
            seen = {}
            count = 0

            for right in range(i, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in word_count:
                    seen[word] = seen.get(word, 0) + 1
                    count += 1

                    while seen[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1

                    if count == total_words:
                        ans.append(left)

                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1

                else:
                    seen.clear()
                    count = 0
                    left = right + word_len

        return ans
    
s = "barfoothefoobarman"
words = ["foo", "bar"]

print(Solution().findSubstring(s, words))