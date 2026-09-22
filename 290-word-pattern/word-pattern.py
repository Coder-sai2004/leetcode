class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        left = {}
        right = {}
        res = [word for word in s.split(' ')]

        if len(pattern) != len(res):
            return False

        for i in range(len(pattern)):
            if pattern[i] in left:
                if left[pattern[i]] != res[i]:
                    return False
            else:
                left[pattern[i]] = res[i]


            if res[i] in right:
                if right[res[i]] != pattern[i]:
                    return False
            else:
                right[res[i]] = pattern[i]

        return True