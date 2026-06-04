class Solution(object):
    def totalWaviness(self, num1, num2):
        wav=0        
        for i in range(num1, num2+1):
            i= str(i)
            if len(i)<3:
                continue
            ij=0
            while ij<len(i)-2:
                if i[ij+1]>i[ij] and i[ij+1]>i[ij+2]:
                    wav+=1
                if i[ij+1]<i[ij] and i[ij+1]<i[ij+2]:
                    wav+=1
                ij+=1
        return wav