from collections import Counter
class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        freq = Counter(s)  # step 1: count frequencies
        groups = {}        # step 2: group by frequency
        for ch, f in freq.items():
            if f not in groups:
                groups[f] = set()
            groups[f].add(ch)
        # step 3: find majority group
        best_size = -1
        best_freq = -1
        best_group = set()
        for f, chars in groups.items():
              size = len(chars)
              if size > best_size or (size == best_size and f > best_freq):
                  best_size = size
                  best_freq = f
                  best_group = chars
        return "".join(best_group)   # step 4: return as string