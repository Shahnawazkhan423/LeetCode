class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]"""
        List1 = []
        for i in range(1,numRows+1):
            row = []
            if i==1:
                row.append(1)
            elif i==2:
                row.append(1)
                row.append(1)
            else:
                prev_row = List1[-1]
                row.append(1)
                for j in range(len(prev_row)-1):
                    Sum = prev_row[j]+prev_row[j+1]
                    row.append(Sum)
                row.append(1)
            List1.append(row)
        return List1