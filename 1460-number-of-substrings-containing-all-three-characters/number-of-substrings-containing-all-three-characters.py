class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        total = 0
        left = 0
        right = 0
        
        count_a = 0
        count_b = 0
        count_c = 0

        while right < len(s):

            # Count current character
            if s[right] == 'a':
                count_a += 1
            elif s[right] == 'b':
                count_b += 1
            else:
                count_c += 1

            # Shrink window when all characters exist
            while count_a > 0 and count_b > 0 and count_c > 0:
                total += len(s) - right

                # Remove leftmost character
                if s[left] == 'a':
                    count_a -= 1
                elif s[left] == 'b':
                    count_b -= 1
                else:
                    count_c -= 1

                left += 1
            
            right += 1

        return total