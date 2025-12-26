class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n=len(customers)
        penalty=[]
        prefix=[0]*n
        suffix=[0]*n
        #if length is 1
        if n==1:
            if customers[0]=='Y': return 1
            else: return 0
        #assigning default values for prefix and suffix
        if customers[0]=='N':
            prefix[0]=1
        if customers[n-1]=='Y':
            suffix[n-1]=1
        #calculating prefix
        for i in range(1,n):
            if customers[i]=='N':
                prefix[i]=prefix[i-1]+1
            else:
                prefix[i]=prefix[i-1]+0
        #calculating suffix
        for i in range(n-2,-1,-1):
            if customers[i]=='Y':
                suffix[i]=suffix[i+1]+1
            else:
                suffix[i]=suffix[i+1]+0
        #calculting penalty
        penalty=[suffix[0]]
        for i in range(n):
            if i==0:
                penalty.append(prefix[i]+suffix[i+1])
            elif i==n-1:
                penalty.append(prefix[i-1])
            else:
                penalty.append(prefix[i]+suffix[i+1])
        #returning index of minimum penalty
        return penalty.index(min(penalty))