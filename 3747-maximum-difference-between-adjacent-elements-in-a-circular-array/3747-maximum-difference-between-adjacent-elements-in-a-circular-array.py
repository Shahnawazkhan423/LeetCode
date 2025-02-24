class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        nums2 = []
        end = len(nums)-1
        for i in range(len(nums)-1):
            start = nums[i]
            End = nums[i+1]
            if i>=0 and i<end:
                Cal = start - End 
                nums2.append(abs(Cal))
        else:
            Cal = nums[end]-nums[0]
            nums2.append(abs(Cal))
        return max(nums2)