class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x : (x[0], -x[1]))
        c=0
        m=0
        for x in intervals:
            if x[1]>m:
                c+=1
                m=x[1]
        return c