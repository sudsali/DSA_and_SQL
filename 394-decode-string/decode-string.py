class Solution:
    def decodeString(self, s: str) -> str:
        numstack = []
        strstack = []
        currnum = 0
        currstr = ""
        for i in s:
            if i.isdigit():
                currnum = currnum * 10 + int(i)
            elif i =='[':
                numstack.append(currnum)
                strstack.append(currstr)
                currnum = 0
                currstr = ""
            elif i == ']':
                num = numstack.pop()
                str1 = strstack.pop()
                currstr = str1 + currstr * int(num)
            else:
                currstr+=i
        return currstr