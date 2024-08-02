class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr = 0 
        maxx = 0
        for i in range(len(gain)):
            curr += gain[i]
            maxx = max(maxx,curr)
        return maxx