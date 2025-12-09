class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        temp = 0 
        
        if temp not in arr:
            return arr
                    
        i = 0 
        while i<len(arr):
            if arr[i]==temp:
                arr.insert(i, temp)
                arr.pop()
                i+=2 
            else:
                i+=1 
        return arr
        