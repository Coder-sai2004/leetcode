class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res=[]
        for i in arr2:
            for j in arr1:
                if i==j:
                    res.append(j)
        l=[item for item in arr1 if item not in arr2]
        return res+sorted(l)