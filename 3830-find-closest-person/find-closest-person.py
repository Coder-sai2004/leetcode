class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        first=abs(z-x)
        second=abs(z-y)
        if first<second:
            return 1
        elif second<first:
            return 2
        else:
            return 0