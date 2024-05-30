class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        if n == 1:
            return nums
        temp = nums[n:]
        for i in range(n):
            ans.append(nums[i])
            ans.append(temp[i])
        return ans