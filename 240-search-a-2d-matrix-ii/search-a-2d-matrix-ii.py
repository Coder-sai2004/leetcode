class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res=[]
        for arr in matrix:
            res.extend(arr)
        if target in res:
            return True
        return False