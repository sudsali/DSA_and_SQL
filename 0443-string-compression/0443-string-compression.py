class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        write = 0
        while read< len(chars):
            char = chars[read]
            count = 0
            while read < len(chars) and chars[read] == char:
                read+=1
                count+=1
            
            chars[write] = char
            write+=1

            if count>1:
                for c in str(count):
                    chars[write] = c
                    write+=1
            
        return write