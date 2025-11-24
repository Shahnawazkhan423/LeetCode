class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = "".join(sorted(ransomNote))
        magazine = "".join(sorted(magazine))
        i=0
        j=0 
        while len(magazine)>j and len(ransomNote)>i:
            if magazine[j]==ransomNote[i]:
                i+=1 
                j+=1
            else:
                j+=1 
        if i==len(ransomNote):
            return True
        else:
            return False