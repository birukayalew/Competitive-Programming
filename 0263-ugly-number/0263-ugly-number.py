class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 1:
            return True
        if n==0:
            return False

        # Divide n by 2, 3, and 5 repeatedly as long as it's divisible
        while n % 2 == 0:
            n //= 2
        while n % 3 == 0:
            n //= 3
        while n % 5 == 0:
            n //= 5

        # If n is reduced to 1, it means its only prime factors were 2, 3, and 5
        return n == 1