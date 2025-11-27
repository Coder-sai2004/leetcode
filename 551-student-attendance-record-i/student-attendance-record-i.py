class Solution:
    def checkRecord(self, s: str) -> bool:
        a=s.count('A')
        c=0
        for i in s:
            if i=='L':
                c+=1
            else:
                c=0
            if c>=3:
                return False
        if a<2:
            return True
        return False