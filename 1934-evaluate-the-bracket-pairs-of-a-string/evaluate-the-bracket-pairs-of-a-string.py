class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        lookup = {}
        result = []

        # Store key-value pairs
        for item in knowledge:
            lookup[item[0]] = item[1]

        key = ''
        pos = 0

        # Process each character
        while pos < len(s):

            if s[pos] == '(':
                pos += 1
                
                # Extract key inside brackets
                while s[pos] != ')':
                    key += s[pos]
                    pos += 1

                # Replace key with its value
                if key in lookup:
                    result.append(lookup[key])
                else:
                    result.append('?')

                key = ''
                pos += 1

            else:
                result.append(s[pos])
                pos += 1

        return "".join(result)