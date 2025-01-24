class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        curr_low = prices[0]
        curr_high = prices[0]
        curr_sum = 0
        for i in range(len(prices)-1):
            curr_sum = prices[i+1] - prices[i]
            if curr_sum > 0:
                profit+= curr_sum
        return profit