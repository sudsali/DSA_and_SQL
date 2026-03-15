class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            res.append(i+1)
        duplicate = set()
        d = 0
        for i in range(len(nums)):
            if nums[i] not in duplicate:
                duplicate.add(nums[i])
            else:
                d = nums[i]
        for i in range(len(res)):
            if res[i] not in duplicate:
                return [d,res[i]]
        return res