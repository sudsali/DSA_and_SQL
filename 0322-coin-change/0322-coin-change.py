class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        visited = set()
        queue = deque()

        queue.append((0,0))
        visited.add(0)

        while queue:
            current_amount, num_of_coins = queue.popleft()

            for coin in coins:
                new_amount = current_amount + coin

                if new_amount == amount:
                    return num_of_coins+1
                
                if new_amount < amount and new_amount not in visited:
                    visited.add(new_amount)
                    queue.append((new_amount,num_of_coins+1))
        
        return -1