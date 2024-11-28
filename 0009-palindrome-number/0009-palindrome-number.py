class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        Temp = x
        rev = 0
        while x!=0 and x>0:
            digi = x%10
            rev = rev*10+digi
            x = x//10
        if Temp==rev:
            return True
        else:
            return False
