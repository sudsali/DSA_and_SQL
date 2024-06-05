class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxval = 0
        for i in range(len(accounts)):
            wealth = 0
            for j in range(len(accounts[0])):
                wealth = wealth + accounts[i][j]
            maxval = max(maxval,wealth)
        return maxval 
        