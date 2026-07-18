"""
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the run-length encoding of countAndSay(n - 1).
Run-length encoding (RLE) is a string compression method that works by replacing each maximal group of 
consecutive identical characters with the concatenation of the length of the group followed by the character itself. 
For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", 
replace "5" with "15", and replace "1" with "11". Thus the compressed string becomes "23321511".

Given a positive integer n, return the nth element of the count-and-say sequence.
"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        
        current_str = "1"
        for _ in range(n - 1):
            next_str = []
            i = 0
            length = len(current_str)
            while i < length:
                count = 1
                while i + 1 < length and current_str[i] == current_str[i + 1]:
                    count += 1
                    i += 1
                next_str.append(str(count))
                next_str.append(current_str[i])
                i += 1
            current_str = "".join(next_str)
            
        return current_str
    
print(Solution().countAndSay(4))