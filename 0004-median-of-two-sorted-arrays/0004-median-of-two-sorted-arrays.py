class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = sorted(nums1 + nums2)
        length = len(nums3)
        mid = length // 2
        if length % 2 != 0:
            return nums3[mid]
        else:
            return (nums3[mid - 1] + nums3[mid]) / 2