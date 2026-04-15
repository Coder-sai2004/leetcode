class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1
        tar=[]
        n=len(words)
        m=float('inf')
        for i in range(n):
            if words[i]==target:
                tar.append(i)
        for i in tar:
            m=min(m,abs(i-startIndex))
            if startIndex>i:
                m=min(m,n-startIndex+i)
            else:
                m=min(m,n-i+startIndex)
        return m