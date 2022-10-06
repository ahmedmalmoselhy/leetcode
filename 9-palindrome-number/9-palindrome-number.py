class Solution(object):
    def isPalindrome(self, x):
        for i,j in zip(str(x), reversed(str(x))):
            if i != j : return False
                
        return True
        