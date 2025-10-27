class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        Count = 0
        i =0
        j =1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    Count+=1 
        return Count