class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
       high = max(candies)
       sum = 0
       res = [False] * len(candies)
       for i in range(len(candies)):
        sum = candies[i]+extraCandies
        if sum >= high:
            res[i] = True
            print(sum)
       return res