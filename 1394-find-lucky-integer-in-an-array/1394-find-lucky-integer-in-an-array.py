class Solution:
    def findLucky(self, arr: List[int]) -> int:
        Set = set(arr)
        Lucky = 0
        for i in Set:
            if arr.count(i)==i and Lucky<i:
                Lucky = i
        
        if Lucky==0:
            return -1
        else:
            return Lucky