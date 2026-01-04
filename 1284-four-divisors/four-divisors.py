import math
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        divisors=[]
        for x in nums:
            sq=int(math.sqrt(x))+1
            temp=[]
            for j in range(1,sq):
                if x%j==0:
                    temp.append(j)
                    temp.append(int(x/j))
            divisors.append(temp)
        s=[set(i) for i in divisors]
        result=[]
        for y in s:
            if len(y)==4:
                result.extend(y)
        return sum(result)