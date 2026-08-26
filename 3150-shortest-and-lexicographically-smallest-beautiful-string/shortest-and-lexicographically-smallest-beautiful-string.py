class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        s+='0'
        i=0
        j=0
        c=0
        res=float('inf')
        ans=''
        while j<len(s):
            while c==k:
                
                if (j-i)==res:
                    res=j-i
                    if s[i:j]<ans:
                        ans=s[i:j]

                elif (j-i)<res:
                    res=j-i
                    ans=s[i:j]

                if s[i]=='1':
                    c-=1
                i+=1

            if s[j]=='1':
                c+=1
            j+=1
    
        return ans