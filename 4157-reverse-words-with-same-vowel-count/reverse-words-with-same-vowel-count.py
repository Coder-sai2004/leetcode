class Solution:
    def reverseWords(self, s: str) -> str:  
        vowels={'a','e','i','o','u'} 
        I=0
        k=0
        for i in s:
            if i in vowels:  I+=1
            elif i==' ':
                k+=1
                break
            k+=1
        i=k
        j=k
        c=0
        ans=s[:k]
        while j<len(s)+1:
            if j==len(s):
                if c==I:
                    ans+=s[i:j][::-1]
                else:
                    ans+=s[i:j]
                break
            if s[j] in vowels:
                c+=1
            elif s[j]==' ':
                if c==I:
                    ans+=s[i:j][::-1]
                else:
                    ans+=s[i:j]
                if j==len(s)-1:
                    ans+=''
                else:
                    ans+=' '
                i=j+1
                c=0
            j+=1
        return ans