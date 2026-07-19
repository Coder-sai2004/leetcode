class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        val=abs((start[0]+start[1])-(target[0]+target[1]))
        if val%2==0:
            return True
        return False