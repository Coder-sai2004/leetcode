class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        c=0
        mx=0
        vowels={'a','e','i','o','u'}
        for i in range(k):
            if s[i] in vowels:
                c+=1
        mx=max(mx,c)

        for i in range(k,len(s)):
            if s[i] in vowels:
                c+=1
            
            if s[i-k] in vowels:
                c-=1

            mx=max(mx,c)
        return mx