class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        res=[]
        for i in range(len(arr)):
            if arr[i]==0:
                res.append(0)
                res.append(0)
            else:
                res.append(arr[i])
        arr[:]=res[:len(arr)]
        