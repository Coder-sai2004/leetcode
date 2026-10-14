class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        s = sum
        k = 0
        ans = ""
        if s < 9:
            ans += str(s)
            k += 1
        else:
            d = s//9
            r = s%9
            ans += "9"*d
            
            if r == 0:
                k += d
            else:
                ans += str(r)
                k += d + 1
        
        if k > num:
            return ""
        else:
            diff = num - len(ans)
            if diff > 0:
                return ans + "0"*diff
            return ans