class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        duplicate = -1
        missing = -1
        
        for num in nums:
            if nums.count(num) == 2:
                duplicate = num
                break

        for i in range(1, n+1):
            if i not in nums:
                missing = i
                break

        return [duplicate, missing]