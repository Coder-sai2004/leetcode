class Solution:
    def canAliceWin(self, n: int) -> bool:
        pos = 0
        stone = 10

        while n >= stone:
            n -= stone
            stone -= 1
            pos += 1
        
        if pos % 2 != 0:
            return True
        return False