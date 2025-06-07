class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        res = 0

        for i in range(k):
            if s[i] in vowels:
                res+=1

        curr_num = res
        for i in range(1,len(s)-k+1):
            if s[i-1] in vowels:
                curr_num-=1
            if s[i+k-1] in vowels:
                curr_num+=1
            res = max(res,curr_num)

        return res