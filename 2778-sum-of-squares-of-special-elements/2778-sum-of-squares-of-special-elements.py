class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        Sum = 0
        for i in range(len(nums)):
            element = nums[i]
            if n%(i+1)==0:
                squr = element**2 
                Sum+=squr 
        return Sum