class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for ind ,val in enumerate(nums):
            rem = target - val
            if rem in hash_map:
                return [hash_map[rem],ind]
            hash_map[val] = ind