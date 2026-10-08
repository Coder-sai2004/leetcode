class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        open_count = 0
        close_count = 0
        result = ''

        # Track parentheses balance
        for char in s:
            if char == '(':
                open_count += 1
            else:
                close_count += 1

            # Reset after a primitive
            if open_count == close_count:
                open_count = 0 
                close_count = 0
            
            # Keep inner parentheses
            if open_count > 1:
                result += char

        if result:
            return result
        return ""