class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr=[pref[0]]
        if len(pref)==0:
            return arr
        for i in range(1,len(pref)):
            a=pref[i]^pref[i-1]
            arr.append(a)
        return arr