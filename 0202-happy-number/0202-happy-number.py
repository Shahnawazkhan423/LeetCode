class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()  

        while n != 1:
            print(f"Current number: {n}")
            current = n
            sum_of_squares = 0

            while current > 0:
                digit = current % 10        
                sum_of_squares += digit ** 2 
                current = current // 10      

            if sum_of_squares in seen:
                return False 

            seen.add(sum_of_squares)
            n = sum_of_squares  
        return True 