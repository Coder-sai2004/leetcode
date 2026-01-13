class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        x=[]
        a=celsius+273.15
        b=celsius*1.80+32.00
        x.append(a)
        x.append(b)
        return x