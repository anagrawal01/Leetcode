class Solution:
    def minElement(self, nums: List[int]) -> int:
        newarr=[]
        for i in nums:
            k=0
            for j in str(i):
                j=int(j)
                k+=j
            newarr.append(k)
        return min(newarr)
