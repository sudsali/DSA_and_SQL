class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        freq = Counter(nums)
        curr = 0
        for i in range(nums[0],nums[-1]+1):
            print(freq[i])
            curr+=freq[i]
            print("curr:",curr)
            if freq[i] > 2:
                j = freq[i] - 2
            else:
                j = 0
            print("j:",j)
            while j > 0:
                nums.remove(i)
                j-=1
        return len(nums)