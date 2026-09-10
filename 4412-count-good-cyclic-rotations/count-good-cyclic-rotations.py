class Solution:
    def pre(self, arr, mid, length):
        res = 0
        prefix = [arr[0]]
        for i in range(1, length):
            prefix.append(prefix[i-1] + arr[i])

        for i in range(mid, length):
            first_half = prefix[i] - prefix[i-mid]
            second_half = prefix[-1] - prefix[i] + prefix[i-mid]
            if first_half > second_half:
                res += 1

        return res

    def countGoodRotations(self, nums: list[int]) -> int:
        length = len(nums)
        mid = length // 2
        left = self.pre(nums, mid, length)
        right = self.pre(nums[mid:] + nums[:mid], mid, length)
        return left + right