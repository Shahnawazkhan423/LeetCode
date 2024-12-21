class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digit2 =[]  
        string = ""
        for i in digits:
            string+=str(i)
            integer = int(string)
            integer+=1
        for j in str(integer):
            digit2.append(int(j))
        return digit2