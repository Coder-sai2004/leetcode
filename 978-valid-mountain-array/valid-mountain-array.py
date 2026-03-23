class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        k=0
        i=0
        if len(arr)<3 or arr[0]>=arr[1]:
            return False
        while i<len(arr)-1:
            if arr[i]==arr[i+1]:
                    return False
            if k==0:
                if arr[i]>arr[i+1]:
                    k+=1
            if k==1:
                if arr[i]<arr[i+1]:
                    return False
            i+=1
        if k==0:
            return False
        return True