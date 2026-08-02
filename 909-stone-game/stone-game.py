class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        i=0
        j=len(piles)-1

        c=0
        alice=0
        bob=0

        while i<j:
            x1=piles[i]
            x2=piles[i+1]
            y1=piles[j]
            y2=piles[j-1]
            if c%2==0:
                if x2<y2:
                    alice+=x1
                else:
                    alice+=y1
            else:
                if x2<y2:
                    alice+=x1
                else:
                    alice+=y1
            i+=1
            j-=1
            c+=1
        if alice>bob:
            return True
        return False