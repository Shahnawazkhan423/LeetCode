class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        Set = set(ransomNote)
        if len(ransomNote) > len(magazine):
                return False
        for i in Set:
            if ransomNote.count(i)> magazine.count(i):
                return False
        
        return True