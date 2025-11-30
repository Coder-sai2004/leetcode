class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        C=[]
        for i in range(1,len(A)+1):
            x=set(A[:i]).intersection(B[:i])
            C.append(len(x))
        return C