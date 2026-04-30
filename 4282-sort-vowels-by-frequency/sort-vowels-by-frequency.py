from collections import Counter
class Solution:
    def sortVowels(self, s: str) -> str:
        vowels_list=[]
        vowels_set={'a','e','i','o','u'}
        chars=list(s)
        vowel_index=0
        #taking vowels found in the string s to vowels_list
        for ch in s:
            if ch in vowels_set:
                vowels_list.append(ch)

        #calculating frequency of vowels and sorting them using lambda based on frequency
        vowel_frequency=Counter(vowels_list)
        sorted_vowel_freq=sorted(vowel_frequency.items(),key=lambda x: x[1],reverse=True)
        sorted_vowels=""
        for vowel, freq in sorted_vowel_freq:
            sorted_vowels+=vowel*freq

        #replacing the vowels position with sorted order
        for i in range(len(chars)):
            if chars[i] in vowels_set:
                chars[i]=sorted_vowels[vowel_index]
                vowel_index+=1
        return "".join(chars)