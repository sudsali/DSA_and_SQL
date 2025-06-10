class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft():
            low,high = 0, len(nums)-1
            index = -1
            while low<=high:
                mid = (low+high)//2
                if nums[mid] < target:
                    low = mid+1
                else:
                    if nums[mid] == target:
                        index = mid
                    high=mid-1
            return index

        def findRight():
            low,high = 0, len(nums)-1
            index = -1
            while low<=high:
                mid = (low+high)//2
                if nums[mid] > target:
                    high = mid-1
                else:
                    if nums[mid] == target:
                        index = mid
                    low=mid+1
            return index

        left = findLeft()
        right = findRight()
        return [left,right]