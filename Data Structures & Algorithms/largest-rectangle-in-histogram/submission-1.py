class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        histStack = []
        maxArea = 0

        for i, height in enumerate(heights):
            lastPoppedIndex = i
            while histStack and height < histStack[-1][1]:
                area = (i - histStack[-1][0]) * histStack[-1][1]
                maxArea = max(maxArea, area)
                lastPoppedIndex = histStack[-1][0]
                histStack.pop()

            histStack.append((i - (i - lastPoppedIndex), height))

        # All of these propogated to the end
        index = len(heights)

        while histStack:
            area = (index - histStack[-1][0]) * histStack[-1][1]
            maxArea = max(maxArea, area)
            histStack.pop()

        return maxArea