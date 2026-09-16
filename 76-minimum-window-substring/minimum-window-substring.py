from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        required = Counter(t)
        ans = ''
        res = float('inf')
        left = 0
        right = 0
        cur = 0
        length = len(s)
        form = 0
        freq = {}
        
        while right < length:
            #adding the values from right side
            if s[right] in required:
                if s[right] in freq:
                    freq[s[right]] += 1
                else:
                    freq[s[right]] = 1
                    
                #duplicate handling, if a certain character frequency in the freq is according to required then that character is fully existed in the freq.
                if freq[s[right]] == required[s[right]]:
                    form += 1
            
            #current window length
            cur += 1
            
            while form == len(required):
                #assigning the minimum window string
                if cur < res:
                    res = cur 
                    ans = s[left : right + 1]
                
                #shrinking from the left side
                if s[left] in freq:
                    if freq[s[left]] == 1:
                        del freq[s[left]]
                        form -= 1
                    else:
                        freq[s[left]] -= 1
                        if freq[s[left]] < required[s[left]]:
                            form -=1
                left += 1
                cur -= 1
            
            right += 1
            
        return ans