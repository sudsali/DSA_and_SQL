class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        checker = set()

        for i in nums:
            if i not in checker:
                checker.add(i)
            else:
                return True
        
        return False