class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        freq = [{} for _ in range(len(nums))]
        max_len = 0

        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                freq[i][diff] = freq[j].get(diff,1) + 1
                max_len = max(max_len,freq[i][diff])
        
        return max_len
