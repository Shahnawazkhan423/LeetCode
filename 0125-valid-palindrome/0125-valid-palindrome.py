class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ch = s.lower()
        char = "".join([item for item in ch if item.isalnum()])
        backword =""
        for i in char:
            backword = i+backword
        if backword==char:
            return True
        else:
            return False