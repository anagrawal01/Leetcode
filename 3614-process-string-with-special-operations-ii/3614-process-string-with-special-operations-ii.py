class Solution:
    def processStr(self, s: str, k: int) -> str:
        n=len(s)
        lengths=[0]*(n+1)
        for i, ch in enumerate(s):
            cur=lengths[i]
            if ch.islower():
                lengths[i+1]=cur+1
            elif ch=="*":
                lengths[i+1]=max(0,cur-1)
            elif ch=="#":
                lengths[i+1]=cur*2
            else:
                lengths[i+1]=cur
        if k>=lengths[n]:
            return '.'
        for i in range(n - 1, -1, -1):
            ch=s[i]
            curlen=lengths[i]
            if ch.islower():
                if k==curlen:
                    return ch
            elif ch=="*":
                pass
            elif ch=="#":
                if k>=curlen:
                    k-=curlen
            else:
                k=curlen-1-k
        return '.'