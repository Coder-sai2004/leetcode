class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        n=num_people
        res=[0]*n
        i=0
        j=1
        while candies>0:
            if j<=candies:
                res[i%n]+=j
                candies-=j
                j+=1
                i+=1
            else:
                res[i%n]+=candies
                candies=0
        return res