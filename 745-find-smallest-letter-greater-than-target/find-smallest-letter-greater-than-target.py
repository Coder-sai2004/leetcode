class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters.append(target)
        s=set(letters)
        letters=sorted(s)
        i=letters.index(target)
        if i>=len(letters)-1:
            return letters[0]
        return letters[i+1]