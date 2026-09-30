class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max = 0
        for x, xvalue in enumerate(heights):
            for y, yvalue in enumerate(heights):
                volume = (min(xvalue, yvalue) * (y - x))
                if volume > max:
                    max = volume
        return max


        