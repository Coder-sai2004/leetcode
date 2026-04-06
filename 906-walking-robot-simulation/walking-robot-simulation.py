class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x = 0
        y = 0
        t = 'n'
        # s is for lookup into the obstacles for the coordinates and res for maximum futhest point
        s = set(tuple(i) for i in obstacles)
        res=tuple()
        temp=[]
        #the below N,E,W,S represents when -1,-2 come,which direction it should go.
        #N- (-1,E) (-2,W)      E- (-1,S) (-2,N)      W- (-1,N) (-2,S)     S- (-1,W) (-2,E)
        for i in commands:
            #North Direction
            if t == 'n':
                if i == -1:
                    t = 'e'
                elif i == -2:
                    t = 'w'
                else:
                    k = 0
                    while k < i:
                        y += 1
                        if (x, y) in s:
                            y -= 1
                            break
                        k += 1
            #East Direction
            elif t == 'e':
                if i == -1:
                    t = 's'
                elif i == -2:
                    t = 'n'
                else:
                    k = 0
                    while k < i:
                        x += 1
                        if (x, y) in s:
                            x -= 1
                            break
                        k += 1
            #West Direction
            elif t == 'w':
                if i == -1:
                    t = 'n'
                elif i == -2:
                    t = 's'
                else:
                    k = 0
                    while k < i:
                        x -= 1
                        if (x, y) in s:
                            x += 1
                            break
                        k += 1
            #South Direction
            elif t == 's':
                if i == -1:
                    t = 'w'
                elif i == -2:
                    t = 'e'
                else:
                    k = 0
                    while k < i:
                        y -= 1
                        if (x, y) in s:
                            y += 1
                            break
                        k += 1
            #the furthest point calculation
            temp.append((x,y))
        res=max(temp,key=lambda x: x[0]**2+x[1]**2)
        return res[0]**2+res[1]**2