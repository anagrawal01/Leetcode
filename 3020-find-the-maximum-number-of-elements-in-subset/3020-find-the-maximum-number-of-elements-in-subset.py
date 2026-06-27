class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        blood= Counter(nums)
        stain= blood.get(1,0)  
        ans= stain if stain%2 else stain-1
        blood.pop(1, None)
        for num in blood:
            res=0
            x=num
            while x in blood and blood[x]>1:
                res+=2
                x*=x
            ans= max(ans, res+(1 if x in blood else -1))
        return ans