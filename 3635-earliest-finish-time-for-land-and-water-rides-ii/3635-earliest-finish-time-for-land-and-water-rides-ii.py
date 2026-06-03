class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        def calc(s1, d1, s2, d2):
            min_end= float('inf')
            for i in range(len(s1)):
                fin= s1[i]+d1[i]
                if fin<min_end:
                    min_end= fin
            ans= float('inf')
            for i in range(len(s2)):
                fin_t= max(min_end, s2[i])+d2[i]
                if fin_t<ans:
                    ans=fin_t
            return ans
        mioaw=calc(landStartTime, landDuration, waterStartTime, waterDuration)
        meow= calc(waterStartTime, waterDuration, landStartTime, landDuration)
        return min(mioaw,meow)