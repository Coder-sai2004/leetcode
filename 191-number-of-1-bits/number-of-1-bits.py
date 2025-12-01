class Solution:
    def hammingWeight(self, n: int) -> int:
        x=format(n,'b')
        return x.count('1')