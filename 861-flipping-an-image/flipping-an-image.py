class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result=[]
        res=[]
        for i in image:
            result.append(i[::-1])
        for x in result:
            x=[1-i for i in x]
            res.append(x)
        return res