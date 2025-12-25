class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happy=sorted(happiness)[::-1]
        selected,count=0,0
        for i in range(k):
            if happy[i]>=count: happy[i]-=count
            else: happy[i]=0
            selected+=happy[i]
            count+=1
        return selected