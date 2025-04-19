class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        start = 0
        if word.isupper() or word.islower():
            return True
        elif word[start].isupper() and  word[start+1:].islower():
           return True

        else:
            return False
