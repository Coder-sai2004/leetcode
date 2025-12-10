import math
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x=math.sqrt(num)
        if int(x)==x:
            return True
        return False