class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m=0
        for x in accounts:
            a=sum(x)
            if a>m:
                m=a
        return m