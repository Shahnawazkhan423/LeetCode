class Solution:
    def findValidPair(self, s: str) -> str:
        for i in range(len(s)-1):
            first = s[i]
            second = s[i+1]
            if first!=second:
                if s.count(first)==int(first) and s.count(second)==int(second):
                    return first+second
        return ""