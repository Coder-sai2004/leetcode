class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area=total_area=0
        i=0
        j=len(height)-1
        while i<j:
            total_area=min(height[i],height[j])*(j-i)
            if total_area>max_area:
                max_area=total_area
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max_area