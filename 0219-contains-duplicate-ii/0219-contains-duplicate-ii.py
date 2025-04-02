class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_dict = {}
        for i in range(len(nums)):
            if nums[i] in index_dict and abs(i-index_dict[nums[i]]<=k):
                return True
            index_dict[nums[i]]=i
        return False