class Solution:
    def reverseDegree(self, s: str) -> int:
        n=123
        reversed_alphabet={}
        j=26
        for i in range(97,n):
            reversed_alphabet[chr(i)]=j
            j-=1
        p=0
        for i in range(len(s)):
            p+=reversed_alphabet[s[i]]*(i+1)
        return p