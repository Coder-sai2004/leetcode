class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        remaining_sum = sum
        digit_count = 0
        result = ""

        # Handle sums smaller than 9
        if remaining_sum < 9:
            result += str(remaining_sum)
            digit_count += 1
        else:
            # Fill digits with 9
            quotient = remaining_sum // 9
            remainder = remaining_sum % 9
            result += "9" * quotient

            if remainder == 0:
                digit_count += quotient
            else:
                result += str(remainder)
                digit_count += quotient + 1

        # Check if the required digits exceed the limit
        if digit_count > num:
            return ""
        else:
            zeros = num - len(result)
            if zeros > 0:
                return result + "0" * zeros
            return result