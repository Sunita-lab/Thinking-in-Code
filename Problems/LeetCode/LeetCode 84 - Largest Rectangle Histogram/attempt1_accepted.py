class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left =[-1]*len(heights)
        right = [len(heights)]*len(heights)
        stack1 = []
        stack2 = []
        areas = [0]*(len(heights))
        for i in range (0, len(heights)):
            while stack1 and heights[stack1[-1]] >= heights[i]:
                stack1.pop()
            left[i] = stack1[-1] if stack1 else -1
            stack1.append(i)
        for i in range (len(heights) - 1, -1, -1):
            while stack2 and heights[stack2[-1]] >= heights[i]:
                stack2.pop()
            right[i] = stack2[-1] if stack2 else len(heights)
            stack2.append(i)

        for i in range (0, len(heights)):
            areas[i] = heights[i] * (right[i] - left[i] - 1)  

        return max(areas)       


            


        