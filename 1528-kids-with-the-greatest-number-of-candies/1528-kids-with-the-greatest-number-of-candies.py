class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxcandy = max(candies)
        res = [0] * len(candies)
        for i in range(len(candies)):
            if (candies[i] + extraCandies) >= maxcandy:
                res[i] = True
            else:
                res[i] = False
        return res