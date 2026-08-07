class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispalindrome(left,right):
            while left<right:
                if s[left]!=s[right]:
                    return False
                else:
                    left+=1
                    right-=1
            return True

        left=0
        right=len(s)-1
        while left<right:
            if s[left]!=s[right]:
                return (
                    ispalindrome(left+1,right) or ispalindrome(left,right-1)
                )
            else:
                left+=1
                right-=1
        return True