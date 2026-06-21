class Solution(object):
    def maxIceCream(self, costs, coins):
        res=0
        costs= sorted(costs)
        for i in costs:
            if i<=coins:
                res+=1
                coins-=i
            else:
                break
        return res