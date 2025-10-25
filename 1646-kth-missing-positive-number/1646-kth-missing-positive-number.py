class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_list = []
        Range_run = arr[-1]+k 
        for i in range(1,Range_run+1):
            if i not in arr:
                missing_list.append(i)
        return missing_list[k-1]