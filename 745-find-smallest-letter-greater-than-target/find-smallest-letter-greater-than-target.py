class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        s=set(letters)
        m=ord(target)+1
        for i in range(m,123):
            if chr(i) in s:
                return chr(i)
        return letters[0]