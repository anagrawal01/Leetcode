class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        res= 0
        for j in sorted(costs):
            if j<=coins:
                res+=1
                coins-=j
            else:
                break
        return res