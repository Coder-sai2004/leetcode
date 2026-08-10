class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res=[0]*(n+2)
        for x in bookings:
            l=x[0]
            r=x[1]+1
            val=x[2]
            res[l]+=val
            res[r]-=val
        temp=res[1:len(res)-1]
        ans=[temp[0]]
        for i in range(1,len(temp)):
            ans.append(ans[i-1]+temp[i])
        return ans