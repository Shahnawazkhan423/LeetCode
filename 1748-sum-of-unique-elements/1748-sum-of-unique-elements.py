class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        unique_element = [items for items in nums if nums.count(items)==1]
        return sum(unique_element)