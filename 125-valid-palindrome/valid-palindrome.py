class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        y=re.sub(r'[^A-Za-z0-9]','',s).lower()
        x=y[::-1]
        if y==x:
            return True
        else:
            return False