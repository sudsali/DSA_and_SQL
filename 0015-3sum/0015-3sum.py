class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                total = nums[l] + nums[r] + nums[i]
                if total == 0:
                    res.add((nums[l],nums[r],nums[i]))
                    l+=1
                    r-=1
                elif total > 0:
                    r-=1
                else:
                    l+=1
        return list(res)