class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n=len(mat[0])
        res=[[0]*n for _ in range(len(mat))]
        s=k%n
        s2=-(k%n)
        c=0
        for x in range(len(mat)):
            if c%2==0:
                res[x][:]=mat[x][s:]+mat[x][:s]
            else:
                res[x][:]=mat[x][s2:]+mat[x][:s2]
            c+=1
            print(res[x])
        if res==mat:
            return True
        return False