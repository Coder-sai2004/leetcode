class Solution:
    def isprime(self, number):
        if number == 1:
            return False

        # Check divisibility up to square root
        for divisor in range(2, int(number**0.5) + 1):
            if number % divisor == 0:
                return False

        return True

    def sumOfPrimesInRange(self, n: int) -> int:
        reversed_num = int(str(n)[::-1])
        start = min(n, reversed_num)
        end = max(n, reversed_num)
        total = 0

        # Sum all primes in the range
        for current_num in range(start, end + 1):
            is_prime = self.isprime(current_num)
            if is_prime:
                total += current_num

        return total