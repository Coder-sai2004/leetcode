class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        i=0
        if ruleKey=='type': i=0
        elif ruleKey=='color': i=1
        else: i=2
        c=0
        for x in items:
            if x[i]==ruleValue:
                c+=1
        return c