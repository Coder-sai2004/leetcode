class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = {}
        mx = 0
        left = 0
        right = 0
        size = 0
        res = 0

        while right < len(nums):
            # Update answer if current window is valid
            if mx <= k:
                res = max(res, size)

            # Add current element to window
            if nums[right] in freq:
                freq[nums[right]] += 1
                mx = max(mx, freq[nums[right]])
                size += 1
            else:
                freq[nums[right]] = 1
                mx = max(mx, freq[nums[right]])
                size += 1

            # Shrink window until frequency becomes valid
            if mx > k:
                while freq[nums[right]] > k:
                    if freq[nums[left]] == 1:
                        del freq[nums[left]]
                    else:
                        freq[nums[left]] -= 1

                    size -= 1
                    left += 1

                mx = freq[nums[right]]

            right += 1

        # Check the final window
        if mx <= k:
            res = max(res, size)

        return res