class Solution:
    def bulbSwitch(self, n: int) -> int:
        if n==0:
            return 0
        i=2
        while n>=i**2:
            i+=1
        return i-1