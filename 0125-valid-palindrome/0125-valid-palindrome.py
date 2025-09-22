class Solution:
    def isPalindrome(self, s: str) -> bool:
        String =""
        for i in s:
            if i.isalpha() or i.isdigit():
                String+=i.lower() 
        if String==String[::-1]:
            return True
        else:
            return False