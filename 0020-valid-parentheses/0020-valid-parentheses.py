class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []
        closePair = {'}':'{',')':'(',']':'['}
        for i in s:
            if stack and i in closePair:
                if stack.pop() != closePair[i]:
                    return False
            else:
                stack.append(i)
        return not stack