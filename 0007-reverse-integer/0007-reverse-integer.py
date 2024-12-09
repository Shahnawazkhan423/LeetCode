class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = x<0
        revers = 0
        rang_1 = -2**31
        rang_2 = 2**31-1
        temp = abs(x)
        
        while temp!=0 and temp>0:
            digit = temp%10
            revers = revers*10+digit
            temp//=10
            if(revers<=rang_1 or revers>=rang_2):
                return 0
        if negative:
            return -revers
        
        return revers
