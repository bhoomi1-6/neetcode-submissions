class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i,j = 0, n-1
        maxarea = 0
        while(i!=j):
            area = abs(min(heights[i],heights[j])*(j-i))
            maxarea = max(maxarea,area)
            if heights[i]<= heights[j]:
                i = i+1
            else:
                j= j-1
        return maxarea

        



        