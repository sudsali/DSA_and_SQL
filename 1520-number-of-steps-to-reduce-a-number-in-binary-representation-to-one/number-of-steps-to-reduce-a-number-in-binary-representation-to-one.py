class Solution:
    def numSteps(self, s: str) -> int:
        #convert binary to decimal
        num = 0
        num = int(s,2)
        #for i in range(len(s)):
        #    mod = c % 10
        #   num = num + (mod*pow(2,i))
        #    c = c // 10
        count = 0
        while num >1:
            if num % 2 == 0:
                num = num // 2
            else:
                num = num + 1
            count+=1
        return count
        