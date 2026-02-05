class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        Min = min(nums)
        Max = max(nums)
        new_list = []
        for i in range(Min, Max):
            if i not in nums:
                new_list.append(i)
        return new_list 