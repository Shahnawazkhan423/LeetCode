class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        Sum = 0
        Len = len(nums)
        index = 0 
        for i in range(len(nums)):
            if i==index:
                index+=1
                if Len%index==0 :
                    sq = nums[i]*nums[i]
                    Sum+=sq
        return Sum