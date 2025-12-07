import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i=0
        a=i**2
        while a<=c:
            y=c-a
            b=math.sqrt(y)
            if b==int(b):
                return True
            i+=1
            a=i**2
        return False