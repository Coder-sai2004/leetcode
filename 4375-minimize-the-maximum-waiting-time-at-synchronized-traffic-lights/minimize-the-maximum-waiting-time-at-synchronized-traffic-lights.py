class Solution:
    def minPenalty(self, period: int, lights: list[int], arrivalTime: list[int]) -> int:
        mx=max(lights)
        res=0
        for val in arrivalTime:
            r=val%period
            if r>=mx:
                res=max(res,period-r)
        return res