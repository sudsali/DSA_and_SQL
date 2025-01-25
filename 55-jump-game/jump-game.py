class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        for i in range(len(nums)-2,-1,-1):
            if n <=(i+nums[i]):
                n = i
        if n == 0:
            return True
        return False