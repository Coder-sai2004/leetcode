class Solution:
    def convert(self,s,k):
        res = []
        i = 0
        j = k
        temp = ""
        cur = 0

        while i < len(s):
            
            if j >= len(s):
                res.append(s[i : ])
            else:
                res.append(s[i : j])

            i += k 
            j += k


        for word in res:
            for ch in word:
                cur += int(ch)
            temp += str(cur)
            cur = 0

        return temp
        
    def digitSum(self, s: str, k: int) -> str:
        ans = ''

        while len(s) > k:
            ans = self.convert(s,k)
            s = ans

        return s