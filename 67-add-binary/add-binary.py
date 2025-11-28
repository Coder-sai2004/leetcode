class Solution(object):
    def addBinary(self, a, b):
        x,y=int(a,2),int(b,2)
        z=x+y
        return bin(z)[2:]