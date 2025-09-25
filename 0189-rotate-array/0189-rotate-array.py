class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start=0
        end = len(nums)
        k = k%end
        while start<k:
            last = nums.pop()
            nums.insert(0,last) 
            start+=1
        return nums
