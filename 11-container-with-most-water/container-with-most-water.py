class Solution:
    def maxArea(self, height: List[int]) -> int:
        L, R = 0, len(height)-1
        maxWater = float('-inf')
        while L<R:
            area = (R-L) * min(height[R],height[L])
            maxWater = max(maxWater, area)
            if height[R] < height[L]:
                R-=1
            else:
                L+=1
        return maxWater
        