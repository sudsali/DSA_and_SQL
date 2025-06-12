class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        while l < r:
            m = (l+r) // 2
            if nums[m] > nums[r]:
                l=m+1
            else:
                r = m

        min_index = l

        if min_index == 0:
            l = 0
            r = n - 1
        elif target >= nums[0] and target <= nums[min_index-1]:
            l = 0
            r = min_index-1
        else:
            l = min_index
            r = n - 1

        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m +1 
            else:
                r = m - 1

        return -1
                
