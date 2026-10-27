class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        return ['.' * n if row == 0 else ('#'*(n - 1) + ('.')) for row in range(m)]