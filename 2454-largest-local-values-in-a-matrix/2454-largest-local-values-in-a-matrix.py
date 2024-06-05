class Solution:
    def MaxVal(self,grid,x,y):
        max_val = 0
        for i in range(x,x+3):
            for j in range(y,y+3):
                max_val = max(max_val,grid[i][j])
        return max_val

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        N = len(grid) - 2
        maxLocal = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                maxLocal[i][j] = self.MaxVal(grid,i,j)
        return maxLocal