class Solutions(object):
    def longestCommonPrefix(self, strs):
        if not str:
            return ""
        first = strs[0]
        
        for i in range (len(first)):
            
            for word in strs[1:]:
                if i == len(word) or word[i]!=first[i]:
                    return first[:i]
        return first

# print(Solutions().longestCommonPrefix(["car","cat","can"]))
