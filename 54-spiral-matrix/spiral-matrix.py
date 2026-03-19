class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1
        left = 0

        i = 0
        res = []

        while top <= bottom and left <= right:
            i = left
            while i <= right:
                res.append(matrix[top][i])
                i += 1

            i = top + 1
            while i <= bottom:
                res.append(matrix[i][right])
                i += 1
            
            if top<bottom:
                i = right - 1
                while i >= left:
                    res.append(matrix[bottom][i])
                    i -= 1

            if left<right:
                i = bottom - 1
                while i > top:
                    res.append(matrix[i][left])
                    i -= 1
    
            top += 1
            right -= 1
            bottom -= 1
            left += 1

        return res