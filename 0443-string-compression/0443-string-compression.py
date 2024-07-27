class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        curr = chars[0]
        count = 0
        if len(chars) == 1:
            return len(chars)
        for i in range(len(chars)):
            if curr != chars[i]:
                s+=curr
                if count > 1:
                    s+=str(count)
                curr = chars[i]
                count = 1
            else:
                count+=1
        s+= curr
        if count > 1:
            s+= str(count)
        print(s)
        chars.clear()
        for i in s:
            chars+=i            
        return len(chars)