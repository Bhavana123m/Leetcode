class Solution(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        stack = []
        max_height = -1
        n = len(heights)
        for i in range(n - 1, -1, -1):
            if heights[i] > max_height:
                stack.append(i)
                max_height = heights[i]
        return stack[::-1]
