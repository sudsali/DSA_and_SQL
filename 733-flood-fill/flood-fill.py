class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def fill(sr,sc,val,color):
            if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
                return

            if image[sr][sc] != val or image[sr][sc] == color:
                return
            image[sr][sc] = color
            
            fill(sr-1,sc,val,color)
            fill(sr+1,sc,val,color)
            fill(sr,sc-1,val,color)
            fill(sr,sc+1,val,color)

        val = image[sr][sc]
        fill(sr,sc,val,color)

        return image