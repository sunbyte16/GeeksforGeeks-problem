class Solution:
    def nthCharacter(self, n):
        digits = 1

        while n > 9 * (10 ** (digits - 1)) * digits:
            n -= 9 * (10 ** (digits - 1)) * digits
            digits += 1

        number = 10 ** (digits - 1) + (n - 1) // digits
        index = (n - 1) % digits

        return str(number)[index]