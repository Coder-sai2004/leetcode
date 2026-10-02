from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_chars = set(order)
        string_chars = Counter(s)
        ordered = ''
        remaining = ''

        # Add characters according to order
        for char in order:
            if char in string_chars:
                ordered += char * string_chars[char]

        # Add remaining characters
        for char in s:
            if char not in order_chars:
                remaining += char
                
        return ordered + remaining