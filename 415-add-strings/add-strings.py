import sys
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num2)<=10**4:
            sys.set_int_max_str_digits(1_000_000)
            x=int(num1)
            y=int(num2)
            z=x+y
            return str(z)