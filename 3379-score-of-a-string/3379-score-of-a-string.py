class Solution:
    def scoreOfString(self, s: str) -> int:
        List1 = []
        Sub = []
        start = 0
        end = 1
        Sum = 0
        for i in s:
            Count= ord(i)
            List1.append(Count)
        while start<end and end<len(List1):
            Subt = List1[start]-List1[end]
            Sub.append(Subt)
            start+=1
            end+=1
        for i in range(len(Sub)):
            Sum+=abs(Sub[i])
        return Sum