class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        temp={}
        temp2={}
        ans=0
        og=set()
        for x in reservedSeats:
            row=x[0]
            seat=x[1]
            og.add(row)

            if 0<seat<6:
                if row in temp:
                    temp[row]=max(temp[row],seat)
                else:
                    temp[row]=seat
            elif 5<seat<11:
                if row in temp2:
                    temp2[row]=min(temp2[row],seat)
                else:
                    temp2[row]=seat
            
        for i in og:
            if (i in temp) or (i in temp2):
                left=1
                right=10

                if i in temp:
                    left=temp[i]
                
                if i in temp2:
                    right=temp2[i]

                val=(right-1)-left
                if (val==4 and (left!=2 and left!=4 and left!=6)) or val>4:
                    ans+= val//4

            elif i not in temp and i not in temp2:
                ans+=2
        
        z=0
        z=(n-len(og))*2
        
        return ans+z