class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        r = 0
        curr_sum = 0
        count = 0
        max_avg = -10000
        first = True

        while r < len(nums):
            curr_sum += nums[r]
            count += 1
            
            if count == k:
                if first:
                    first = False
                else:
                    curr_sum -= nums[l]
                    l += 1

                max_avg = max(max_avg, curr_sum / k)
                count -= 1

            r += 1
        return max_avg