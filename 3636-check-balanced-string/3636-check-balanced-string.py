class Solution:
    def isBalanced(self, num: str) -> bool:
        even = 0
        odd = 0
        for i in range(len(num)):
            digit = ord(num[i]) - ord('0')
            if i%2==0:
                even+=digit
            else:
                odd+=digit
        if even==odd:
            return True
        else:
            return False
