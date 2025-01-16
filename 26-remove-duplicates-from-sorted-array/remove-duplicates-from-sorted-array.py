class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = []
        for i in nums:
            if i not in temp:
                temp.append(i)
        nums.clear()
        for i in temp:
            nums.append(i)
        return len(nums)