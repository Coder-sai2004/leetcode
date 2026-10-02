class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        s = set(dictionary)
        res = []
        left = 0
        right = 0
        n = len(sentence)

        while right < n:
            while right < n and sentence[right] != ' ':
                right += 1

                if sentence[left:right] in s:
                    res.append(sentence[left:right])

                    while right < n and sentence[right] != ' ':
                        right += 1

                    right += 1
                    left = right
                    break

            if left != right:
                res.append(sentence[left:right])
                right += 1
                left = right

        return " ".join(res)