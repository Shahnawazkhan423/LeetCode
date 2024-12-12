class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {
            "]":"[",
        "}":"{",
        ")":"(",
        }
        stack =[]
        index=0
        for i in s:
            if index==0:
                stack.append(i)
                index+=1
                continue
            if i in mapping and stack[index-1]==mapping[i]:
                stack.pop()
                index-=1
            else:
                stack.append(i)
                index+=1
        if stack:
            return False
        else:
            return True