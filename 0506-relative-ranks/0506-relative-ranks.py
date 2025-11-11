class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores = sorted(score, reverse=True)
        medal = []

        for s in score:
            rank = sorted_scores.index(s)
            if rank == 0:
                medal.append("Gold Medal")
            elif rank == 1:
                medal.append("Silver Medal")
            elif rank == 2:
                medal.append("Bronze Medal")
            else:
                medal.append(str(rank + 1))
        
        return medal