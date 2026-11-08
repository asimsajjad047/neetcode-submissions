class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        max = 0
        current = 0
        while l < r:
            current = (min(heights[l], heights[r]) * (r-l))
            if current >= max:
                max = current
            if heights[r] > heights[l]:
                l = l+1
            else:
                r = r-1
        return max