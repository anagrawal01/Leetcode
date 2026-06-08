class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pew=[]
        khekhe= []
        gng= []
        for i in nums:
            if i<pivot:
                pew.append(i)
            elif i>pivot:
                khekhe.append(i)
            else:
                gng.append(i)
        pew.extend(gng)
        pew.extend(khekhe)
        
        return pew
        