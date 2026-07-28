class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        b=0
        for i in range(len(nums)):
            a=nums[i]
            for j in range(i+1,len(nums)):
                if (a==nums[j]):
                    b+=1
        if b>0:
            return True
        else:
            return False