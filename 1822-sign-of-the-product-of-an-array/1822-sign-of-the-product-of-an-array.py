class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0

        # Step 2: Count negative numbers
        negative_count = 0
        for num in nums:
            if num < 0:
                negative_count += 1

        # Step 3: Decide sign based on negative count
        if negative_count % 2 == 0:
            return 1
        else:
            return -1