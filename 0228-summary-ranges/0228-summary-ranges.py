class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        List = []
        Sy = "->"
        i = 0

        while i < len(nums):
            j = 1
            while i + j < len(nums) and nums[i + j] == nums[i] + j:
                j += 1
            
            if j > 1:
                Comb = str(nums[i]) + Sy + str(nums[i + j - 1])
                List.append(Comb)
            else:
                List.append(str(nums[i]))
            
            i += j

        return List
