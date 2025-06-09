class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = m * n - 1

        while low <= high:
            mid = (low+high)//2
            row,col = divmod(mid,n)
            mid_val = matrix[row][col]

            if target == mid_val:
                return True
            elif mid_val < target:
                low = mid+1
            else:
                high = mid-1

        return False
            