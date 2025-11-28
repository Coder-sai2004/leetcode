from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp=defaultdict(list)
        for word in strs:
            key=tuple(sorted(word))
            grp[key].append(word)
        return list(grp.values())