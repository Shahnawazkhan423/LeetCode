class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums3 = []
        for i in set(nums1):
            if i in nums2:
                nums3.append(i)
        return nums3
