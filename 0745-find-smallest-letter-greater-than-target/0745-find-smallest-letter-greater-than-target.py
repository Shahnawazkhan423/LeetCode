class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start = 0
        end = len(letters) - 1
        res = letters[0] 

        while start <= end:
            mid = (start + end) // 2
            if letters[mid] > target and letters[mid]!=target:
                res = letters[mid]  
                end = mid - 1
            else:
                start = mid + 1
    
        return res