class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        freq = Counter(nums)
        curr = 0
        j = 0
        for i in range(nums[0],nums[-1]+1):
            curr+=freq[i]
            if freq[i] > 2:
                j = freq[i] - 2
            while j > 0:
                nums.remove(i)
                j-=1
        return len(nums)