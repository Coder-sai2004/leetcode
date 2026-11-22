class Solution:
    def checkString(self, s: str) -> bool:
        b = False

        for ch in s:
            if ch == 'b':
                b = True
            
            if b > 0 and ch == 'a':
                return False

        return True