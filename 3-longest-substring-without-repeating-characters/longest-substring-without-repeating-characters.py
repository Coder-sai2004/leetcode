from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x=deque()
        y=set()
        c=0
        for i in s:
            while i in y:
                rm=x.popleft()
                y.remove(rm)
            x.append(i)
            y.add(i)
            if c<len(x):
                c=len(x)
        return c