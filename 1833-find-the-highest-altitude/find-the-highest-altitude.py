class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        pre=[gain[0]]
        for i in range(1,len(gain)):
            pre.append(pre[i-1]+gain[i])
        m=max(pre)
        return max(m,0)