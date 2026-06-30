class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count=[0]*3
        bae=0
        res=0
        for i,j in enumerate(s):
            count[ord(j)-ord('a')]+=1
            while all(count):
                res+=len(s)-i
                count[ord(s[bae])-ord('a')]-=1
                bae+=1
        return res
        