class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        i= 0 
        j=1 
        count = 0 
        while len(nums)>j:
            first = nums[i:j]
            sec = nums[j:]
            Sum = sum(first)
            Sum1 = sum(sec)
            total = Sum - Sum1 
            if total%2==0:
                count+=1 
            j+=1
        return count