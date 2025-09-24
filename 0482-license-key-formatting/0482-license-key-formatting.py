class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-","").upper()
        parts = []
        while len(s)>k:
            parts.insert(0,s[-k:])
            s= s[:-k]
        if s:
            parts.insert(0,s)
        return "-".join(parts)