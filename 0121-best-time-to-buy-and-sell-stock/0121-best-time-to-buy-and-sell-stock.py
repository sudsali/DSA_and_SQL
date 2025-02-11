class Solution:
    # here we need to keep track of the minimum cost and if current price is greater than min_cost we calculate max profit
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_buy = prices[0]
        for i in range(len(prices)):
            min_buy = min(min_buy,prices[i])
            if prices[i] > min_buy:
                profit = max(profit,prices[i]-min_buy)
        return profit
