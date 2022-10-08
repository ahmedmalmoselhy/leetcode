class Solution(object):
    def reverseVowels(self, s):
        vowellist = set(['a','e','i','o','u','A','E','I','O','U'])
    
        s = list(s)
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and s[l] not in vowellist:
                l += 1
            while r > l and s[r] not in vowellist:
                r -= 1

            s[l],s[r] = s[r],s[l]
            l += 1
            r -= 1

        return "".join(s)
        