class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time=0
        for i in range(len(points)-1):
            x=points[i]
            y=points[i+1]
            time+=max(abs(x[0]-y[0]),abs(x[1]-y[1]))
        return time