class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        res=[]
        s=set(bulbs)
        for i in s:
            if bulbs.count(i)%2==0:
                continue
            else:
                res.append(i)
        res.sort()
        return res