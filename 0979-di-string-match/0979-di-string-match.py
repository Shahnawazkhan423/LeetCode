class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low,high = 0,len(s)
        result =[] 
        for i in s:
            if i=="I":
                result.append(low)
                low+=1
        
            else:
                result.append(high)
                high-=1 
        if low==high:
            result.append(high)
        return result 