class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res=[]
        mi=float('inf')
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]<mi:
                mi=arr[i+1]-arr[i]
        for j in range(len(arr)-1):
            if arr[j+1]-arr[j]==mi:
                res.append([arr[j],arr[j+1]])
        return res