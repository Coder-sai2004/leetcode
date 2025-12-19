class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        stack=[]
        for i in s:
            if stack and stack[-1]!=i:
                stack.pop()
            else:
                stack.append(i)
        return len(stack)