class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1 = {}
        for i in nums:
            if i not in dict1:
                dict1[i]=1 
            else:
                dict1[i]+=1


        grep = 0
        keys = 0
        for key,val in dict1.items():
            if val>grep:
                grep=val
                keys = key

        return keys