class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # Add extra 0 for the end case
        s += '0'
        left = 0
        right = 0
        count = 0
        length = float('inf')
        ans = ''
        
        while right < len(s):
            while count == k:
                # If lengths match, choose the smaller substring
                if (right - left) == length:
                    if s[left:right] < ans:
                        ans = s[left:right]

                # If shorter, assign immediately
                elif (right - left) < length:
                    length = right - left
                    ans = s[left:right]

                # Shrink window from the left
                if s[left] == '1':
                    count -= 1
                left += 1

            # Count 1's in the window
            if s[right] == '1':
                count += 1
            right += 1
        
        return ans