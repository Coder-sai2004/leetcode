class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        s = sum
        k = 0
        ans = ""
        while s > 0:
            if s > 9:
                ans += "9"
                s -= 9
            else:
                ans += str(s)
                s = 0
            k += 1
        
        if k > num:
            return ""
        else:
            diff = num - len(ans)
            if diff > 0:
                return ans + "0"*diff
            return ans