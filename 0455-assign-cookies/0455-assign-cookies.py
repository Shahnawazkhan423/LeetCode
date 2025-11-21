class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()  
        s.sort()
        i = 0 
        j = 0
        Count = 0
        while len(g)>i and len(s)>j:
            if g[i]<=s[j]:
                Count+=1 
                i+=1 
                j+=1
            else:
                j+=1
        return Count