# class Solution(object):
#     def totalWaviness(self, num1: int, num2: int) -> int:
#         def solve(num:int) -> int: 
#             if num<100:
#                 return 0
#             n= len(str(num))

#             memo_cnt= [[[-1]*10 for _ in range(10)] for _ in range(16)]
#             memo_sum= [[[-1]*10 for _ in range(10)] for _ in range(16)]

#             from functools impory lru_cache
#             @lru_cache(None)
#             def dfs(
#                 pos: int, prev: int, curr: int, isLimit: bool, isLeading: bool
#             ):
#                 if pos==n:
#                     return 1, 0

class Solution(object):
    def totalWaviness(self, num1, num2):

        def solve(n):
            if n <= 0:
                return 0

            s = str(n)
            memo = {}

            def dfs(pos, prev2, prev1, waves, tight, started):
                key = (pos, prev2, prev1, waves, tight, started)

                if key in memo:
                    return memo[key]

                if pos == len(s):
                    return waves

                limit = int(s[pos]) if tight else 9
                ans = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    if not started and d == 0:
                        ans += dfs(pos + 1, -1, -1, waves,
                                   ntight, False)
                        continue

                    if not started:
                        ans += dfs(pos + 1, -1, d, waves,
                                   ntight, True)
                        continue

                    nwaves = waves

                    if prev2 != -1:
                        if ((prev1 > prev2 and prev1 > d) or
                            (prev1 < prev2 and prev1 < d)):
                            nwaves += 1

                    ans += dfs(pos + 1, prev1, d, nwaves,
                               ntight, True)

                memo[key] = ans
                return ans

            return dfs(0, -1, -1, 0, True, False)

        return solve(num2) - solve(num1 - 1)