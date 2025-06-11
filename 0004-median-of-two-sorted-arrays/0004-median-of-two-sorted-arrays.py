class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p1 = 0
        p2 = 0
        i=0
        total_len = len(nums1) + len(nums2)
        is_even = (total_len % 2 == 0)
        mid = total_len // 2

        res = []
        while len(res) <= mid:
            if p1 < len(nums1) and (p2 >= len(nums2) or nums1[p1] <= nums2[p2]):
                res.append(nums1[p1])
                p1+=1
            else:
                res.append(nums2[p2])
                p2+=1

        if is_even:
            median = (res[-1]+res[-2])/2
        else:
            median = res[-1]

        return median