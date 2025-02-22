class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        n = len(nums)
        total = 0
        for i in range(len(nums)):
            is_good = True
            if i-k>=0:
                if nums[i]<=nums[i-k]:
                    is_good = False
            if i+k<n:
                if nums[i]<=nums[i+k]:
                    is_good = False
            if is_good:
                total+=nums[i]
        return total