class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s)<=k:
            return s[::-1]
        temp=list(s)
        i , j , a ,b ,res= 0, k*2 , k, k*2, []
        while i<=len(s):
            res+=((temp[i:k])[::-1]+temp[k:j])
            i=j
            k=j+a
            j+=b
        return "".join(res)