class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = ""
        def compare(a,b):
            if str(a) + str(b)  > str(b) + str(a):
                return -1
            elif str(a) + str(b)  < str(b) + str(a):
                return 1
            else:
                return 0
        
        nums.sort(key=cmp_to_key(compare))
        if nums[0] == 0:
            return "0"

        for i in nums:
            res+=str(i)
        return res

            