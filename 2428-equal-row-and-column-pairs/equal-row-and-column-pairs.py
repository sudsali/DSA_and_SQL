class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = grid
        cols = []
        count = 0
        for k in range(len(grid)):
            col = []
            for i in range(len(grid)):
                col.append(grid[i][k])
            cols.append(col)
        for i in rows:
            for j in cols:
                if i ==j:
                    count+=1
        return count
