class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list_n = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                targ = nums[i]+nums[j]
                if target==targ:
                    list_n.append(i)
                    list_n.append(j)
        return list_n
   