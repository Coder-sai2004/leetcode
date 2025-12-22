from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        start=0
        window_size=len(words[0])
        substring_size=len(words)*window_size
        res=[]
        word_freq=Counter(words)
        for offset in range(window_size):
            start=offset
            end=offset+substring_size
            while start+substring_size<=len(s):
                sub=s[start:end]
                if Counter([sub[m:m+window_size] for m in range(0,len(sub),window_size)])==word_freq:
                    res.append(start)
                start+=window_size
                end=start+substring_size
        return res