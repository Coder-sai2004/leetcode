from collections import defaultdict,Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        #taking counter for frequency and default dict for grouping words based on count
        freq=Counter(words)
        group=defaultdict(list)
        for word,count in sorted(freq.items(),key=lambda x: x[1], reverse=True):
            group[count].append(word)
        res=[]
        #sorting the words into lexicographical order
        for x in group.values():
            res.extend(sorted(x))
        return res[:k]