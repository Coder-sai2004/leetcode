class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        x=sorted(heights)
        c=0
        for i in range(len(heights)):
            if x[i]!=heights[i]:
                c+=1
        return c