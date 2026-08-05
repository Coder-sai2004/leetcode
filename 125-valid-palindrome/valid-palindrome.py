class Solution(object):
    def isPalindrome(self, s):
        temp=''
        for i in s:
            if i.isalnum():
                temp+=i.lower()
        print(temp,temp[::-1])
        if temp==temp[::-1]:
            return True
        return False