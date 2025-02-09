class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [numbers.index(numbers[l])+1,len(numbers)-numbers[::-1].index(numbers[r])]
            elif numbers[l] + numbers[r] > target:
                r-=1
            else:
                l+=1
        return []