class Solution:
    def nextGreaterElement(self, n: int) -> int:
        res = [int(i) for i in str(n)]
        i = len(res) - 2
        j = len(res) - 1

        while i >= 0 and res[i] >= res[i + 1]:
            i -= 1
        
        if i < 0:
            return -1

        while res[j] <= res[i]:
            j -= 1

        res[i],res[j] = res[j],res[i]

        res[i + 1:] = reversed(res[i + 1:])

        res = [str(i) for i in res]

        ans = int("".join(res))

        if ans <= 2**31 - 1:
            return ans
        return -1