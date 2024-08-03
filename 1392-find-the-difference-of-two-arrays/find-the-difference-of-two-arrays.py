class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res1 , res2 = [],[]
        nums1 , nums2 = set(nums1),set(nums2)
        for i in nums1:
            if i not in nums2:
                res1.append(i)
        for i in nums2:
            if i not in nums1:
                res2.append(i)  
        return [res1 , res2]
