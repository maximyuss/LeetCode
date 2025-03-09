# https://leetcode.com/problems/closest-prime-numbers-in-range/
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def isPrime(num):
            if num == 2 or num == 3: return True
            if num < 2 or num % 2 == 0: return False
            divisor = 3
            while divisor * divisor <= num:
                if num % divisor == 0: return False
                divisor += 2
            return True

        prev_prime = -1
        closestA = -1
        closestB = -1
        min_difference = float("inf")

        for candidate in range(left, right + 1):
            if isPrime(candidate):
                if prev_prime != -1:
                    difference = candidate - prev_prime
                    if difference < min_difference:
                        min_difference = difference
                        closestA = prev_prime
                        closestB = candidate
                    if difference == 1 or difference == 2:
                        return [prev_prime, candidate]
                prev_prime = candidate

        return [closestA, closestB] if closestA != -1 else [-1, -1]
