class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewl2 = set(jewels)
        count = 0
        for i in stones:
            if i in jewl2:
                count+=1
        return count