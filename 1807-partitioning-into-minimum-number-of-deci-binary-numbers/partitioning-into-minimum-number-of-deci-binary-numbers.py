class Solution:
    def minPartitions(self, n: str) -> int:
        for x in "9876543210":
            if x in n:
                return int(x)