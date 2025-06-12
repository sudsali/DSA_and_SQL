class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pivot = n - 1

        def swap(nums,pivot,index):
            temp = nums[pivot]
            nums[pivot] = nums[index]
            nums[index] = temp
            return

        while pivot >=1 and nums[pivot] <= nums[pivot-1]:
            pivot-=1
        
        if pivot!=0:
            i = n-1
            while nums[i]<=nums[pivot-1]:
                i-=1
            swap(nums,pivot-1,i)
        
        left = pivot
        right = n -1
        while left < right:
            swap(nums,left,right)
            left+=1
            right-=1
