class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Set = set(s)
        flag = False
        if len(s)!=len(t):
            return False
        for i in Set:
            if s.count(i) == t.count(i):
                flag = True 
            else:
                flag = False
                break 
        return flag