class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score=0
        counter=0
        for i in events:
            if counter==10:
                break
            if i=="WD" or i=="NB":
                score+=1
            elif i=="0" or i=="1" or i=="2" or i=="3" or i=="4" or i=="6":
                score+=int(i)
            elif i=="W":
                counter+=1
        return [score,counter]