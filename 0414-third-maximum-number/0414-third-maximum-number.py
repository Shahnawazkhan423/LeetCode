class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        Uniq = []
        for j in range(len(nums)):
            if nums[j] not in Uniq:
                Uniq.append(nums[j])
        Uniq.sort(reverse=True)
        if len(Uniq)<3:
            return Uniq[0]
        else:
            return Uniq[2]
