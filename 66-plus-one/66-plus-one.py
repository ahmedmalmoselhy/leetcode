class Solution(object):
    def plusOne(self, digits):
        buffString = ""
        for i in digits:
            buffString = buffString + str(i)
        buffString = str(int(buffString) + 1)
        alist = [int(i) for i in buffString]
        return(alist)
