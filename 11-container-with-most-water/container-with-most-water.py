class Solution:
    def maxArea(self, height: List[int]) -> int:
        L = 0
        R = len(height)-1
        global_max = float('-inf')
        while L<R:
            area = (R-L) * min(height[L],height[R])
            global_max = max(area, global_max)
            if height[R]<height[L]:
                R-=1
            else:
                L+=1
        return global_max
        