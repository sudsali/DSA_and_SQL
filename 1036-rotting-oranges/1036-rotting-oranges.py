class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_count = 0
        queue = deque()
        rows, cols = len(grid) , len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c,0))
                elif grid[r][c] == 1:
                    fresh_count+=1

        res_min = 0
        directions = [(1,0),(0,-1),(-1,0),(0,1)]
        
        while queue:
            r, c , res_min = queue.popleft()
            for dr,dc in directions:
                new_r, new_c = r+dr,c+dc
                if (new_r >= 0 and new_r < rows) and (new_c >=0 and new_c < cols) and grid[new_r][new_c]==1:
                    grid[new_r][new_c]=2
                    fresh_count-=1
                    queue.append((new_r,new_c,res_min+1))
            
        if fresh_count != 0:
            return -1

        return res_min


