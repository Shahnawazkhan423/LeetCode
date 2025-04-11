class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        elif s == goal:
            if len(set(s)) < len(s):
                return True
            else:
                return False
        else:
            diff = []
            for a, b in zip(s, goal):
                if a != b:
                    diff.append((a, b))
            if len(diff) == 2 and diff[0] == diff[1][::-1]:
                return True
            else:
                return False
                    

