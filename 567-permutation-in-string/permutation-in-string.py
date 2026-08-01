class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge case: if s2 is shorter than s1, it cannot contain any permutation.
        if len(s2) < len(s1):
            return False

        # cur_freq stores the frequency of characters in the current window.
        # target_freq stores the frequency of characters in s1.
        cur_freq = {}
        target_freq = {}

        # Calculate the frequency of characters in s1.
        for ch in s1:
            target_freq[ch] = target_freq.get(ch, 0) + 1

        # Window size is equal to the length of s1.
        k = len(s1)

        # Calculate the frequency of characters in the first window of s2.
        for i in range(k):
            cur_freq[s2[i]] = cur_freq.get(s2[i], 0) + 1

        # Check whether the first window is a permutation of s1.
        result = True
        for key in target_freq.keys():
            # If a character is missing or its frequency doesn't match,
            # the current window is not a permutation.
            if key not in cur_freq or target_freq[key] != cur_freq[key]:
                result = False

        if result:
            return result

        # Slide the window one character at a time and check each window.
        for i in range(k, len(s2)):
            result = True

            # Remove the leftmost character from the current window.
            if cur_freq[s2[i - k]] == 1:
                del cur_freq[s2[i - k]]
            else:
                cur_freq[s2[i - k]] -= 1

            # Add the new rightmost character to the current window.
            cur_freq[s2[i]] = cur_freq.get(s2[i], 0) + 1

            # Check whether the current window is a permutation of s1.
            for key in target_freq.keys():
                if key not in cur_freq or target_freq[key] != cur_freq[key]:
                    result = False

            if result:
                return result

        return False