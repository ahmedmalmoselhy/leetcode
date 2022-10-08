class Solution(object):
    def longestCommonPrefix(self, strs):
        match = 0
        
        for vals in zip(*strs):
            if len(set(vals)) == 1:
                match += 1
            else:
                break
        
        return strs[0][:match]
        