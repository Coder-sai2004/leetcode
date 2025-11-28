class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        x=list(s.strip())
        x.reverse()
        c=0
        for i in x:
            print(i)
            if i==' ':
                break
            c+=1
        return c