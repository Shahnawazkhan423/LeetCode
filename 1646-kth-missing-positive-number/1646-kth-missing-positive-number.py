class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        start,end = 0,len(arr)-1 
        while start<=end:
            mid_point = (start+end)//2
            if arr[mid_point]-mid_point-1<k:
                start = mid_point+1 
            else:
                end = mid_point-1 
        return start+k