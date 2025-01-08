import math
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        max_len = 0
        for i in range(len(nums)):
            prod = 1
            gcd_val = nums[i]
            lcm_val = nums[i]
            
            for j in range(i, len(nums)):
                print(nums[j])
                prod *= nums[j]
                
                gcd_val = math.gcd(gcd_val, nums[j])
                
                lcm_val = (lcm_val * nums[j]) // math.gcd(lcm_val, nums[j])

                if prod == lcm_val * gcd_val:
                    max_len = max(max_len, j - i + 1) 
        return max_len