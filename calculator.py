class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def negate(self, a):
        return self.subtract(0, a)

    def multiply(self, a, b):
        negative = (a < 0) != (b < 0)
        a, b = abs(a), abs(b)

        result = 0
        for _ in range(b):
            result = self.add(result, a)

        return self.negate(result) if negative else result

    def _int_divide(self, a, b):
        count = 0
        while a >= b:
            a = self.subtract(a, b)
            count = self.add(count, 1)
        return count, a

    def divide(self, a, b, decimals=15):
        if b == 0:
            return "cannot divide by zero"

        negative = (a < 0) != (b < 0)
        a, b = abs(a), abs(b)

        whole, remainder = self._int_divide(a, b)

        digits = ""
        for _ in range(decimals):
            if remainder == 0:
                break
            remainder = self.multiply(remainder, 10)
            digit, remainder = self._int_divide(remainder, b)
            digits += str(digit)

        result = float(f"{whole}.{digits or '0'}")
        return self.negate(result) if negative else result

    def modulo(self, a, b):
        if b == 0:
            raise ZeroDivisionError("cannot take modulo by zero")

        _, r = self._int_divide(abs(a), abs(b))
        if r != 0 and (a < 0) != (b < 0):
            r = self.subtract(abs(b), r)
        return self.negate(r) if b < 0 else r


# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: multiplication: ", calc.multiply(-5, -5))
    print("Example: multiplication: ", calc.multiply(-5, 5))
    print("Example: multiplication: ", calc.multiply(-5, 0))
    print("Example: division: ", calc.divide(10, 3))
    print("Example: division: ", calc.divide(0, 2))
    print("Example: division: ", calc.divide(-5, -4))
    print("Example: modulo: ", calc.modulo(10, 3))
