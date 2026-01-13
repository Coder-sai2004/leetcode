class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        r=sorted(score,key=lambda x:x[k])
        return r[::-1]