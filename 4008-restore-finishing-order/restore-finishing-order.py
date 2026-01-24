class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        s=set(friends)
        res=[]
        for i in order:
            if i in s:
                res.append(i)
        return res