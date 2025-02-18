class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        for i in range(len(s)-k+1):
            substring = s[i:i+k]
            if len(set(substring))==1:
                before = s[i-1] if i>0 else None
                after = s[i+k] if i+k<len(s) else None
                if (before != substring[0]) and (after != substring[0]):
                    return True
        return False