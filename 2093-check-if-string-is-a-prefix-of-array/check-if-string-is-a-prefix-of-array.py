class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        t=''
        for i in words:
            t+=i
            if t==s:
                return True
        return False