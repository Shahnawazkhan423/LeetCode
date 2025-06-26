class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_str = ""
        for i in digits:
            num_str += str(i)
        
        result = int(num_str) + 1
        
        return [int(d) for d in str(result)]
