class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        #taken c_col and c_row for readability and tracking of current cells
        c_col=cStart
        c_row=rStart
        visited_cells=[]

        #vertical and horizontal represents the limit of their ends
        vertical=1
        horizontal=2

        #layers represents how many times we need to rotate
        layers=max(c_col,c_row,abs(cols-c_col),abs(rows-c_row))

        #directions represents the various directions we move
        directions=5
        visited_cells.append([c_row,c_col])
        for _ in range(layers):
            for phase_index in range(directions):
                if phase_index==0: #move right once
                    c_col+=1
                    if c_row<rows and c_col<cols and c_row>=0 and c_col>=0:
                        visited_cells.append([c_row,c_col])
                elif phase_index==1: #moves bottom until it reachs its limit
                    i=0
                    while i<vertical:
                        c_row+=1
                        if c_row<rows and c_col<cols and c_row>=0 and c_col>=0:
                            visited_cells.append([c_row,c_col])
                        i+=1 
                elif phase_index==2 or phase_index==3 or phase_index==4:
                    #moves left,top,right until it reaches its limit
                    j=0
                    while j<horizontal:
                        if phase_index==2:    c_col-=1
                        elif phase_index==3:  c_row-=1
                        else:       c_col+=1
                        if c_row<rows and c_col<cols and c_row>=0 and c_col>=0:
                            visited_cells.append([c_row,c_col])
                        j+=1
                        
            #increasing limit after each layer completion
            vertical+=2
            horizontal+=2
        return visited_cells