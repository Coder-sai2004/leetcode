class Solution:
    def minRotations(self, s: str) -> int:
        total = 0
        current = 0
        digits = [int(i) for i in s]

        # Process each digit
        for digit in digits:
            if current == digit:
                total += 0
            else:
                # Calculate minimum rotation
                if current < digit:
                    total += min(digit - current, (10 + current) - digit)
                else:
                    total += min(current - digit, (10 + digit) - current)

                current = digit

        return total