class Solution:
    def check(self, arr , index):
        max_length = 0
        i = index
        curr_length = 1

        # Check alternating increasing and decreasing pairs
        while i < len(arr) - 1:
            if i % 2 == 0 and arr[i] < arr[i + 1]:
                curr_length += 1
            elif i % 2 != 0 and arr[i] > arr[i + 1]:
                curr_length += 1
            else:
                max_length = max(curr_length, max_length)
                curr_length = 1

            i += 1

        max_length = max(curr_length, max_length)

        return max_length

    def maxTurbulenceSize(self, arr: list[int]) -> int:
        result1 = self.check(arr , 0)
        result2 = self.check([0] + arr , 1)

        print(result1,result2)

        return max(result1, result2)