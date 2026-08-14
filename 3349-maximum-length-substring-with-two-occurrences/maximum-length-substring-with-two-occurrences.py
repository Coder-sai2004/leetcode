class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = {}
        mx = 0
        left = 0
        right = 0
        size = 0
        res = 0
        k=2

        while right < len(s):
            # Update answer if current window is valid
            if mx <= k:
                res = max(res, size)

            # Add current element to window
            if s[right] in freq:
                freq[s[right]] += 1
                mx = max(mx, freq[s[right]])
                size += 1
            else:
                freq[s[right]] = 1
                mx = max(mx, freq[s[right]])
                size += 1

            # Shrink window until frequency becomes valid
            if mx > k:
                while freq[s[right]] > k:
                    if freq[s[left]] == 1:
                        del freq[s[left]]
                    else:
                        freq[s[left]] -= 1

                    size -= 1
                    left += 1

                mx = freq[s[right]]

            right += 1

        # Check the final window
        if mx <= k:
            res = max(res, size)

        return res