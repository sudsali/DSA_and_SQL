class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove_indices = set()
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    remove_indices.add(i)

        stack = []
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ')':
                stack.append(i)
            elif s[i] == '(':
                if stack:
                    stack.pop()
                else:
                    remove_indices.add(i)

        result = []
        for i, char in enumerate(s):
            if i not in remove_indices:
                result.append(char)

        return ''.join(result)
                
                
        