class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Edge case: if s is shorter than p, it cannot contain any anagram.
        if len(s) < len(p):
            return []
            
        # anagram is to track the current window for checking if it is an anagram
        # target is the original required characters and their frequency
        current_freq = {}
        target_freq = {}

        # calculating the target frequency
        for ch in p:
            target_freq[ch] = target_freq.get(ch, 0) + 1

        # k is the window size
        k = len(p)

        # first window calculation
        for i in range(k):
            current_freq[s[i]] = current_freq.get(s[i], 0) + 1

        ans = []
        result = True

        # check whether the first window is an anagram
        for key in target_freq.keys():
            # if key is missing or the frequency doesn't match,
            # then this window is not an anagram
            if key not in current_freq or target_freq[key] != current_freq[key]:
                result = False

        if result:
            ans.append(0)

        # from the second window onwards
        for i in range(k, len(s)):
            result = True

            # shrinking or reducing the characters from the left side
            if current_freq[s[i - k]] == 1:
                del current_freq[s[i - k]]
            else:
                current_freq[s[i - k]] -= 1

            # adding the character from the right side
            current_freq[s[i]] = current_freq.get(s[i], 0) + 1

            for key in target_freq.keys():
                if key not in current_freq or target_freq[key] != current_freq[key]:
                    result = False

            if result:
                ans.append(i - k + 1)

        return ans