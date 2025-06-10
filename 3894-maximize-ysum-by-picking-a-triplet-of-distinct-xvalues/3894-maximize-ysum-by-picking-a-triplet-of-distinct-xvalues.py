class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        x_to_y_max = {}
        for xi, yi in zip(x,y):
            x_to_y_max[xi] = max(x_to_y_max.get(xi,float('-inf')),yi)

        heap = []

        for y in x_to_y_max.values():
            if len(heap) < 3:
                heapq.heappush(heap,y)
            else:
                if y > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap,y)

        if len(heap) < 3:
            return -1
        else:
            return sum(heap)
