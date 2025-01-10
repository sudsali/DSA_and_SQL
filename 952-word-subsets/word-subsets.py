class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_freq = {}
        for word in words2:
            curr = collections.Counter(word)
            for i in curr:
                if i in max_freq:
                    max_freq[i] = max(max_freq[i],curr[i])
                else:
                    max_freq[i] = curr[i]
        res = []
        for word in words1:
            freq = collections.Counter(word)
            count = 0
            for i in freq:
                if i in max_freq and freq[i] >= max_freq[i]:
                    count+=1
            if count == len(max_freq):
                res.append(word)
        return res