from collections import defaultdict
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #res is used for grouping the elements with the closest difference
        #idx is used later for index iteration
        #kclose is the resultant list
        res=defaultdict(list)
        idx=0
        kclose=[]

        #here we are grouping the value based on difference between them
        for i in arr:
            diff=abs(i-x)
            res[diff].append(i)

        #sorting the res based the difference (smallest/closest first)
        temp=sorted(res.items(),key=lambda x:x[0])

        #adding the closest k elements in the list
        while len(kclose)<k:
            kclose.extend(temp[idx][1])
            idx+=1

        return sorted(kclose[:k])