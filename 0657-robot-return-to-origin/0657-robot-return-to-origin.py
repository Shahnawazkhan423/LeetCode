class Solution:
    def judgeCircle(self, moves: str) -> bool:
        U = 0 
        D = 0 
        L = 0 
        R = 0 
        for i in moves:
            if i=="U" :
                U+=1 
            elif i=="D":
                D+=1
            elif i=="L":
                L+=1 
            else:
                R+=1
        if U==D and L==R:
            return True
        else:
            return False
