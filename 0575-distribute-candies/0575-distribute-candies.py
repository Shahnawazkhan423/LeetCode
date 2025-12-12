class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        Len  = len(candyType)
        Set = set(candyType)
        Divi = Len//2
        Min = min(len(Set), Divi)
        return Min
