class Solution:
    def reverseWords(self, s: str) -> str:  
        #taking vowels for checking frequency
        vowels={'a','e','i','o','u'} 
        words=[word for word in s.split()]
        n=0
        res=[]
        for i in words[0]:
            if i in vowels:
                n+=1
        res.append(words[0])
        #reversing the words that has same count of vowels as first word
        for i in range(1,len(words)):
            c=0
            for j in words[i]:
                if j in vowels:
                    c+=1
            if c==n:
                res.append(words[i][::-1])
            else:
                res.append(words[i])
        return " ".join(res)