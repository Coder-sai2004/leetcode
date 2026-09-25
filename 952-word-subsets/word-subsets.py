from collections import Counter
class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        max_freq = {}
        subset_counts = []
        word_counts = []
        result = []

        # Count characters in words1
        for word in words1:
            word_counts.append(Counter(word))

        # Count characters in words2
        for word in words2:
            subset_counts.append(Counter(word))

        # Store maximum required frequency
        for subset in subset_counts:
            for char, freq in subset.items():
                max_freq[char] = max(max_freq.get(char, 0), freq)
        
        # Check each word against required frequencies
        for i in range(len(word_counts)):
            word_count = word_counts[i]
            is_valid = True

            for char, freq in max_freq.items():
                if char not in word_count or word_count[char] < max_freq[char]:
                    is_valid = False
                    break

            if is_valid:
                result.append(words1[i])
        
        return result