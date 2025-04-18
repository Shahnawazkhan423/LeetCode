class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1 = {}
        for i in nums:
            if i in dict1:
                dict1[i]+=1 
            else:
                dict1[i]=1 

            max_value = max(dict1, key=dict1.get)
        return max_value
