class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #we will use backtracking for this
        # only add ( if openN < n
        # only add ) if closedN < openN
        # Valid res iff openN == closedN == n
        stack = []
        res = []
        def backtracking(openN,closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append('(')
                backtracking(openN + 1, closedN)
                stack.pop()
            
            if closedN < openN:
                stack.append(')')
                backtracking(openN, closedN + 1)
                stack.pop()

        backtracking(0,0)
        return res
            