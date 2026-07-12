class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        s1=startTime.split(":")
        s2=endTime.split(":")
        start=0
        end=0
        for i in range(len(s1)):
            temp1=int(s1[i])
            temp2=int(s2[i])
            #hours converts into seconds and assigned to x,y
            if i==0:
                x=temp1*60*60
                y=temp2*60*60
            #minutes converts into seconds and assigned to x,y
            elif i==1:
                x=temp1*60
                y=temp2*60
            #seconds assigned to x,y
            elif i==2:
                x=temp1
                y=temp2
            start+=x
            end+=y
        return end-start