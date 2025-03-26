class Solution:
    def dailyTemperatures(self, temperatures):
        # - We use a stack to keep track of indices of temperatures in decreasing order.  
        # - As we process each temperature, we check if it is greater than the temperature at the top of the stack.  
        # - If it is, we pop elements from the stack and update the result for those indices with the number of days waited.  
        # - If no warmer temperature is found for a day, the result remains 0 (already initialized).  
        # - The stack ensures each element is processed at most twice (push & pop), making this an O(n) solution.
        stack = []
        res = [0] * len(temperatures)
        for i,temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index
            stack.append(i)
        return res