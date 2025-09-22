class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        Sum1 = sum(ord(i) for i in s)
        Sum2 = sum(ord(i) for i in t)
        return chr(Sum2 - Sum1)