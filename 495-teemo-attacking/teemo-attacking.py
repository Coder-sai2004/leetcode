class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        x=len(timeSeries)
        possible=x*duration
        y=duration-1
        temp=[]
        tmerge=0
        temp=timeSeries
        for i in range(len(temp)-1):
            c=temp[i]+y+1
            n=c-temp[i+1]
            if n>0:
                tmerge+=n
        return possible-tmerge