class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        x="".join(word1)
        y="".join(word2)
        if x==y:
            return True
        return False