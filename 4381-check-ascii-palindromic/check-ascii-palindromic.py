class Solution:
    def isPalindromic(self, s: str) -> bool:
        ans=''
        for ch in s:
            binary=format(ord(ch),'b')
            string=binary.zfill(8)
            ans+=string
        if ans==ans[::-1]:
            return True
        return False