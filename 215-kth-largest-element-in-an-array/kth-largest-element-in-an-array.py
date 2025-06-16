class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for i in nums:
            heapq.heappush(heap,-i)

        while k>0:
            res = heapq.heappop(heap)
            k-=1
        
        return res * -1