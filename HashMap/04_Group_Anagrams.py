"""
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.
"""

class Solution(object):
    def groupAnagrams(self, strs):

        groups = {}

        for word in strs:

            key = "".join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))