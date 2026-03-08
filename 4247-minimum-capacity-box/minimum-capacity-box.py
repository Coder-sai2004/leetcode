class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        m=float('inf')
        idx=-1
        for i in range(len(capacity)):
            if capacity[i]>=itemSize:
                if capacity[i]<m:
                    m=capacity[i]
                    idx=i
        return idx