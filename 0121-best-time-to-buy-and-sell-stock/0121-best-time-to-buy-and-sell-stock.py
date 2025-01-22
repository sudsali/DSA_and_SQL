class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = prices[0]
        high = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < low:
                low = prices[i]
                high = prices[i]
            elif prices[i] > high:
                if prices[i] - low > profit:
                    profit = prices[i] - low
        return profit