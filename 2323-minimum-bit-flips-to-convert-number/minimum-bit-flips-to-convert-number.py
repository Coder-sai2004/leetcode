class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        a=format(start,'b')
        b=format(goal,'b')
        m=max(len(a),len(b))
        a=a.zfill(m)
        b=b.zfill(m)
        f=0
        for i in range(len(a)):
            if a[i]!=b[i]:
                f+=1
        return f