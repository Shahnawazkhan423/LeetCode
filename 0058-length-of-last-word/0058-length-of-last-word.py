class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        txt = s.strip().split()
        return len(txt[-1])