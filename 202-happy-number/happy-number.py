class Solution:
    def isHappy(self, n: int) -> bool:
        x=n
        z=0
        while z!=1 and z!=4:
            x=str(x)
            z=0
            for i in range(len(x)):
                a=int(x[i])
                z+=a**2
            x=z
        if z==1:
            return True
        else:
            return False