class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<=1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        mi=intervals[0][0]
        mx=intervals[0][1]
        n=len(intervals)-1
        res=[]
        for i in range(1,len(intervals)):
            cur_mi=intervals[i][0]
            cur_mx=intervals[i][1]
            if cur_mi<mx and cur_mx<mx:
                if i==n:
                    res.append([mi,mx])
                continue
            elif cur_mi<=mx:
                mx=cur_mx
            elif mx<cur_mi:
                res.append([mi,mx])
                mi=cur_mi
                mx=cur_mx
                
            if i==n:
                    res.append([mi,mx])
        return res