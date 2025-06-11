class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        right = [[0]* cols for _ in range(rows)]
        down = [[0]* cols for _ in range(rows)]

        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                if grid[i][j] == 1:
                    right[i][j] = 1 + (right[i][j+1] if j+1 < cols else 0)
                    down[i][j] = 1 + (down[i+1][j] if i+1 < rows else 0)
        
        max_square = 0
        for i in range(rows):
            for j in range(cols):
                for size in range(min(rows-i,cols-j),0,-1):
                    if (right[i][j] >= size and down[i][j] >= size and right[i+size-1][j] >=size and down[i][j+size-1]>=size):
                        max_square = max(max_square,size)
                        break
        
        return max_square * max_square