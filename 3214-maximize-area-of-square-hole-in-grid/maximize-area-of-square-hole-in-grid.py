class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        #taken variables that are needed
        maxHstreak=maxVstreak=0
        currHstreak=currVstreak=0
        #calculating longest sequence of consecutive integers of hBars
        if n==1:  maxHstreak=1
        else:
            for i in range(len(hBars)-1):
                if hBars[i]+1==hBars[i+1]: currHstreak+=1
                else:
                    maxHstreak=max(maxHstreak,currHstreak+1)
                    currHstreak=0
            maxHstreak=max(maxHstreak,currHstreak+1)
        #calculating longest sequence of consecutive integers of hBars
        if m==1:  maxVstreak=1
        else:
            for i in range(len(vBars)-1):
                if vBars[i]+1==vBars[i+1]:  currVstreak+=1
                else:
                    maxVstreak=max(maxVstreak,currVstreak+1)
                    currVstreak=0
            maxVstreak=max(maxVstreak,currVstreak+1)
        #calculating side length and returning area of it
        side=min(maxHstreak+1,maxVstreak+1,n+1,m+1)
        return side**2