class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        first = 0
        sec = 1

        while first<sec and sec<len(nums):
            if nums[first]==nums[sec]:
                nums.pop(sec)
            else:
                first+=1 
                sec+=1 

            

        return len(nums) 