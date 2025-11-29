class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x=[]
        for sub in matrix:
            x.extend(sub)
        if target in x:
            return True
        else:
            return False