class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        #minutes degree
        m=minutes*6
        #hour degree
        h=(hour*30)+minutes*0.5
        angle1=abs(m-h)
        angle2=abs(360-angle1)
        return min(angle1,angle2)