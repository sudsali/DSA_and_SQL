class Solution:
    def interpret(self, command: str) -> str:
        s = ""
        for i in range(len(command)):
            if command[i] == '(' and command[i+1] == ')':
                s+='o'
            else:
                s+=command[i]
        s = s.replace("(","")
        s= s.replace(")","")
        return s