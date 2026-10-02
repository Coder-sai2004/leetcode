class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        s = set(dictionary)
        res = []
        x = ''
        i = 0
        n = len(sentence)
        
        while i < n:
            while i < n and sentence[i] != ' ':
                x += sentence[i]
                i += 1
                
                if x in s:
                    
                    res.append(x)
                    x = ''
                    while i < n and sentence[i] != ' ':
                        i += 1
                    i += 1
                    
                    break

            if len(x) != 0:
                res.append(x)
                x = ''
                i += 1

        return " ".join(res)