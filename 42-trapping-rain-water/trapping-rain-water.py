class Solution:
    def trap(self, height: List[int]) -> int:

        # find 2 arrs: max_left for each index and max_right for each index
        # Then water will be sum of min(max_left[i],max_right[i]) - height[i]
        # remember to not consider the last index when calculating water 
        water = 0
        max_left = [0] * len(height)
        max_right = [0] * len(height)

        max_right[-1] = height[-1]
        for i in range(len(height)-2,-1,-1):
            max_right[i] = max(max_right[i+1],height[i])
            
        max_left[0] = height[0]
        for i in range(1,len(height)):
            max_left[i] = max(max_left[i-1],height[i])

        for i in range(len(height)-1):
            water += min(max_left[i],max_right[i]) - height[i]
        return water