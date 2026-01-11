from collections import Counter
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        #win and lose taken for seperating winners and losers
        win,lose=[],[]
        for x in matches:
            win.append(x[0])
            lose.append(x[1])

        #undefeated and once_defeated taken for calculating their respectives values
        undefeated,once_defeated=[],[]
        x=Counter(lose)
        s=set(lose)

        #checking for undefeated players
        for i in win:
            if i not in s:
                undefeated.append(i)

        #checking for once defeated players
        for i in lose:
            if x[i]==1:
                once_defeated.append(i)

        #removing duplicates and returning the values in increasing order
        w=set(undefeated)
        l=set(once_defeated)
        return sorted(list(w)),sorted(list(l))