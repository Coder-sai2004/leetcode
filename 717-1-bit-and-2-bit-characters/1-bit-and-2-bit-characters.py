class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n=len(bits)
        x=[]
        i=0
        while i<n:
            if bits[i]==0:
                x.append(bits[i])
                i+=1
            elif bits[i]==1:
                x.append(bits[i])
                i+=2
        r=len(x)-1
        if x[r]==0:
            return True
        return False
