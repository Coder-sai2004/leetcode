import numpy as np
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        s=set()
        m=np.array(matrix)
        t=m.T
        for i in range(1,len(matrix)+1):
            s.add(i)
        for j in range(len(matrix)):
            if len(set(matrix[j]))==len(s) and len(set(t[j]))==len(s):
                continue
            else:
                return False
        return True