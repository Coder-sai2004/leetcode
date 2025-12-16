class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        b=False
        c=candies
        ex=extraCandies
        rs=[]
        for i in c:
            x=i+ex
            if max(c)<=x:
                b=True
                rs.append(b)
            else:
                b=False
                rs.append(b)
        return rs