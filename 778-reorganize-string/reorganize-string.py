class Solution:
    def reorganizeString(self, s: str) -> str:
        res = ""
        counter = collections.Counter(s)
        if any(freq > (len(s) + 1) // 2 for freq in counter.values()):
            return ""

        heap = []
        for k,v in counter.items():
            heapq.heappush(heap,(-v,k))
        
        prev_char , prev_count = "",0

        while heap:
            freq, char = heapq.heappop(heap)
            res+=char
            if prev_count < 0:
               heapq.heappush(heap,(prev_count,prev_char))
            
            prev_char, prev_count = char, freq+1
            
        return res