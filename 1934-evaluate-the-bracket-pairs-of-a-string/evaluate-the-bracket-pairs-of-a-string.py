class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        lookup = {}
        parts = []
        
        # Store key-value pairs
        for entry in knowledge:
            lookup[entry[0]] = entry[1]
        
        current = ''
        index = 0

        # Split text and bracketed keys
        while index < len(s):

            if s[index] == '(':
                if current != '':
                    parts.append(current)
                    current = ''

                while s[index] != ')':
                    current += s[index]
                    index += 1

                index += 1
                parts.append(current)
                current = ''

            else:
                current += s[index]
                index += 1
        
        if current != '':
            parts.append(current)

        # Replace keys with their values
        for i in range(len(parts)):
            first_char = parts[i][0]
            key = parts[i][1:]

            if first_char == '(':
                if key in lookup:
                    parts[i] = lookup[key]
                else:
                    parts[i] = '?'

        return "".join(parts)