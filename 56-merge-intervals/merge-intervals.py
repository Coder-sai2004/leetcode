class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        #sorting the intervals based on the first value of the interval
        intervals.sort(key=lambda x: x[0])

        mi = intervals[0][0]
        mx = intervals[0][1]
        n = len(intervals) - 1
        res = []

        for i in range(1, len(intervals)):
            cur_mi = intervals[i][0]
            cur_mx = intervals[i][1]

            # if the current intervals is in between the previous intervals
            if cur_mi < mx and cur_mx < mx:
                if i == n:
                    res.append([mi, mx])
                continue

            # if the current and previous intervals overlap
            elif cur_mi <= mx:
                mx = cur_mx

            # if the current and previous intervals not related
            elif mx < cur_mi:
                res.append([mi, mx])
                mi = cur_mi
                mx = cur_mx

            if i == n:
                res.append([mi, mx])

        return res