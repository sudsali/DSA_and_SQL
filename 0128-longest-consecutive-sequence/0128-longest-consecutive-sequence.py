class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        temp = set()
        res = 0
        for i in nums:
            hashset.add(i)

        for i in hashset:
            count = 1
            if i+1 not in temp:
                while i+1 in hashset:
                    temp.add(i+1)
                    count+=1
                    i+=1
            res = max(res,count)

        return res