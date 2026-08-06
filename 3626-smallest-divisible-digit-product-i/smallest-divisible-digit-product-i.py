class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        val=1
        temp=n
        while temp>0:
            x=temp%10
            val*=x
            temp=temp//10
        
        while val%t!=0:
            n+=1
            temp=n
            val=1
            while temp>0:
                x=temp%10
                val*=x
                temp=temp//10
        return n