class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = {}
        cur_sum = 0
        ans=0

        # Add distinct values to the sum for the first window of size k.
        for i in range(k):
            if nums[i] not in freq:
                cur_sum += nums[i]
            freq[nums[i]] = freq.get(nums[i], 0) + 1

        # If the number of distinct elements equals the window size,
        # then the current window is a valid distinct subarray.
        if len(freq.keys()) == k:
            ans = max(ans, cur_sum)

        for i in range(k, len(nums)):
            # Shrink the window by removing the leftmost element.
            if freq[nums[i - k]] == 1:
                del freq[nums[i - k]]
                #here we remove nums[i-k] from cur_sum only when its frequency is equal to 1
                cur_sum-=nums[i-k]
            else:
                freq[nums[i - k]] -= 1

            # Add the new element to the sum only if it is not already
            # present in the current window.
            if nums[i] not in freq:
                cur_sum += nums[i]

            freq[nums[i]] = freq.get(nums[i], 0) + 1

            # If all elements in the current window are distinct,
            # update the maximum sum.
            if len(freq.keys()) == k:
                ans = max(ans, cur_sum)

        return ans