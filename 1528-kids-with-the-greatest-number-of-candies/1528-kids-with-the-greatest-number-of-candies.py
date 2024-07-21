class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
       high = max(candies)
       res = [False] * len(candies)
       for i in range(len(candies)):
        if candies[i]+extraCandies >= high:
            res[i] = True
       return res