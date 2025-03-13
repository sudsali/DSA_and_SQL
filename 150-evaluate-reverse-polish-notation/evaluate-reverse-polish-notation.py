class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == '+':
                temp1 = stack.pop()
                temp2 = stack.pop()
                stack.append((temp1+temp2))
            elif i == '*':
                temp1 = stack.pop()
                temp2 = stack.pop()
                stack.append((temp1*temp2))
            elif i == '-':
                temp1 = stack.pop()
                temp2 = stack.pop()
                stack.append((temp2-temp1))
            elif i == '/':
                temp1 = stack.pop()
                temp2 = stack.pop()
                stack.append(int(temp2/temp1))
            else:
                stack.append(int(i))
        return stack[0]