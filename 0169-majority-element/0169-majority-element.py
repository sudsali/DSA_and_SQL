class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        for i in freq:
            if freq[i] > ((len(nums)-1)//2):
                return i