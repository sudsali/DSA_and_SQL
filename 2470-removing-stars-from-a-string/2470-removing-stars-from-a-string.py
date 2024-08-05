class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        s1 = ""
        for i in s:
            if i == '*':
                stack.pop()
            else:
                stack.append(i)
        for i in stack:
            s1+=i
        return s1
        