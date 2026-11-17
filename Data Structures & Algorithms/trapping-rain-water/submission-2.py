class Solution:
    def trap(self, height: List[int]) -> int:
        
        maxRightArr = {}
        max_right = 0
        for i in range(len(height)-1, -1, -1):
            maxRightArr[i] = max_right
            max_right = max(max_right, height[i])


        maxLeftArr = {}
        max_left = 0
        water = 0
        for i in range(len(height)):
            maxLeftArr[i] = max_left
            max_left = max(max_left, height[i])
            min_h = min(maxRightArr[i], maxLeftArr[i])
            c = min_h - height[i]
            if c > 0:
                water += c

        return water




