class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxA = 0

        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxA = max(maxA, (i - index)*height)
                start = index
            stack.append((start, h))
        
        while stack:
            i, h = stack.pop()
            maxA = max(maxA, (len(heights) - i)*h)
        return maxA
            
        