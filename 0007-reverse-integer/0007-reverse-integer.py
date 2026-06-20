class Solution(object):
    def reverse(self, x):
        abx=str(abs(x))
        rev=int(abx[::-1])
        if x<0:
            rev=-rev
        if rev <-2**31 or rev> 2**31-1:
            return 0
        return rev