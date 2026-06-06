class Solution(object):
    def leftRightDifference(self, nums):
        leftsum= []
        rightsum=[]
        rightsum.append('l')
        leftsum.append('j')
        answer=[]
        for j in range(len(nums)):
            if leftsum[0]=='j':
                leftsum[0]=0
                leftsum.append(nums[0])
            else:
                k= leftsum[j]+nums[j]
                leftsum.append(k)
            
        for p in range(len(nums)):
            if rightsum[0]=='l':
                rightsum[0]=0
                rightsum.insert(0, nums[-1])
            else:
                l= rightsum[0]+nums[-1-p]
                rightsum.insert(0, l)
        
        leftsum.pop() 
        rightsum.pop(0)
        for n in range(0, len(nums)):
            tururu= leftsum[n]-rightsum[n]
            answer.append((abs(tururu)))
        
        return answer
    