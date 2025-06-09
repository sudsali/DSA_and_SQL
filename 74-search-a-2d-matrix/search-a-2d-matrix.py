class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        found = False
        new_r = 0
        new_c = 0

        for i in range(m):
            if target<=matrix[i][n-1]:
                new_r = i
                new_c = n-1
                break

        for r in range(new_r+1):
            for c in range(new_c+1):
                if target == matrix[r][c]:
                    found = True

        return found
