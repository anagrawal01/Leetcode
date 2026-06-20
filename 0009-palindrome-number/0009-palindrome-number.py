class Solution(object):
    def isPalindrome(self, x):
        y=[]
        for i in str(x)[::-1]:
            y.append(i)
        k= "".join(y)
        return k==str(x)
        