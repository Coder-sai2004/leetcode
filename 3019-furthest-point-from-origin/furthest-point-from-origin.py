class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l=moves.count('L')
        r=moves.count('R')
        d=0
        if l==r:
            moves=moves.replace('_','R')
        elif l>r:
            moves=moves.replace('_','L')
        else:
            moves=moves.replace('_','R')
            
        for i in moves:
            if i=='L':
                d-=1
            else:
                d+=1
        return abs(d)