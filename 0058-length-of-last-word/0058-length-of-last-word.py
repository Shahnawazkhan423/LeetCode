class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        txt = s.split()
        length = 0
        for i in txt[-1]:
            length+=1
        return length