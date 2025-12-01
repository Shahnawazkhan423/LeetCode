class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dup = set(nums)
        list1 = []
        for i in range(1,len(nums)+1):
            if i not in dup:
                list1.append(i) 
        return list1