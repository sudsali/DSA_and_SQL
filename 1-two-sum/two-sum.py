class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = nums
        nums = sorted(nums)
        s = 0
        e = len(nums) - 1
        fin = []
        while s < e:
            if nums[s] + nums[e] > target:
                e-=1
            elif nums[s] + nums[e] < target:
                s +=1
            else:
                ans = [nums[s],nums[e]]
                break
        for i in ans:
            fin.append(temp.index(i))
            temp[temp.index(i)] = -1
        return fin