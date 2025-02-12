class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        left = prices[0]
        max_pro = 0
        for i in range(1,len(prices)):
            if prices[i]<left:
                left = prices[i]
            else:
                max_pro = max(max_pro,prices[i]-left)
        return max_pro