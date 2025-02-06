class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=2:
            while k > 0:
                nums.reverse()
                k-=1
        else:
            temp = nums[:(len(nums)-k)]
            nums.extend(temp)
            for i in range(len(temp)):
                nums.pop(0)