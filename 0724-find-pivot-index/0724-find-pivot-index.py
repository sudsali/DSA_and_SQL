class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums[1:])
        ans = 0
        for i in range(len(nums)-1):
            if left == right:
                ans = i
                return ans
            else:
                left+=nums[i]
                right-=nums[i+1]
        left = sum(nums[:-1])
        right = 0
        if left == right:
            return len(nums)-1
        return -1
