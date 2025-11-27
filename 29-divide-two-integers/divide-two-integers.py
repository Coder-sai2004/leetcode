class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==0 or dividend<divisor and dividend>0:
            return 0
        x=int(dividend/divisor)
        if x==0:
            return 0
        elif x>0 and x<=2**31-1:
            return x
        elif x>0:
            return 2**31-1
        elif x<0 and x>=-2**31:
            return x
        elif x<0:
            return -2**31
        