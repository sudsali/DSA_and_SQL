class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if not s:
            return 0

        res = 0
        is_negative = False
        i= 0
        int_min = -2**31
        int_max = (2**31) - 1
        if s[i] == '-' or s[i] == '+':
            if s[i] == '-':
                is_negative = True
            i+=1
        while i < len(s) and s[i].isdigit():
                res = res * 10 + int(s[i])
                i+=1
        if is_negative:
            res = -1 * res

        if res < int_min:
            return int_min
        if res > int_max:
            return int_max    
        return res