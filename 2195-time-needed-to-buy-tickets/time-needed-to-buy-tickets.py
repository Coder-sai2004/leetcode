class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        c=0
        i=0
        while tickets[k]!=0:
            if tickets[i]==0:
                i+=1
                if i==len(tickets):
                    i=0
                continue
            else:
                tickets[i]-=1
                c+=1
            i+=1
            if i==len(tickets):
                i=0
        return c