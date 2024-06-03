class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        pos = 0
        ans = []
        for i in words:
            if x in i:
                ans.append(pos)
            pos+=1
        return ans
        