class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        Split = text.split()
        third = []
        i = 0 
        j = 1 
        while i<j and len(Split)>j:
            if Split[i]==first and Split[j]==second and len(Split)>j+1:
                data = Split[j+1]
                third.append(data)
            i+=1 
            j+=1 
        return third