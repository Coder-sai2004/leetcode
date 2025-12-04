class Solution:
    def reverseVowels(self, s: str) -> str:
        st=list(s)
        l,r=0,len(st)-1
        v={'a','e','i','o','u','A','E','I','O','U'}
        while l<=r:
            if st[l] in v and st[r] in v:
                st[l],st[r]=st[r],st[l]
                l+=1
                r-=1
            elif st[l] in v:
                r-=1
            else:
                l+=1
        x=''.join(st)
        return x