class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = []
        pos = 0
        for j in words[0]:
            count = 0
            for i in range(1,len(words)):
                if j in words[i]:
                    count+=1
                    pos = words[i].index(j)
                    words[i] = words[i][:pos]+ words[i][pos+1:]
            if count == (len(words)-1):
                ans.append(j)
        return ans
