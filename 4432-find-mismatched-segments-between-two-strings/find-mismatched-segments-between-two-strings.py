class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        first_index = 0
        second_index = 0
        result = []
        first_segment = ""
        second_segment = ""

        # Compare both strings character by character
        while first_index < len(s1) and second_index < len(s2):
            if s1[first_index] == s2[second_index]:

                # Store the mismatched segment when matching characters are found
                if len(first_segment) > 0:
                    result.append([first_segment, second_segment])
                    first_segment = ""
                    second_segment = ""

            else:
                # Collect characters that do not match
                first_segment += s1[first_index]
                second_segment += s2[second_index]

            first_index += 1
            second_index += 1

        # Store the remaining mismatched segment, if any
        if len(first_segment) > 0:
            result.append([first_segment, second_segment])

        return result