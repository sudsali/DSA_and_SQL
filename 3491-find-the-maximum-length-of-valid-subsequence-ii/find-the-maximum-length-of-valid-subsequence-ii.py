class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        freq = [{} for _ in range(len(nums))]
        max_len = 1

        for i in range(len(nums)):
            for j in range(i):
                mod = (nums[j] + nums[i]) % k
                freq[i][mod] = max(freq[i].get(mod, 1), freq[j].get(mod, 1) + 1)
                max_len = max(max_len, freq[i][mod])
        
        return max_len