class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_differ = 0
        n = len(nums)
        max_differ = max(max_differ,abs(nums[0]-nums[-1]))
        for i in range(1,n):
            max_differ = max(max_differ,abs(nums[i]-nums[i-1]))
        return max_differ
