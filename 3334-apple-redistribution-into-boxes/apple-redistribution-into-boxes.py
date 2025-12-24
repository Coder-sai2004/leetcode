class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        x=sorted(capacity)[::-1]
        s=sum(apple)
        c,t=0,0
        for i in x:
            t+=i
            c+=1
            if t>=s: return c