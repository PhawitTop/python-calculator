class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        for _ in range(abs(b)):
            result = self.add(result, a)
        if b < 0:
            result = -result
        return result

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot be 0")
        result = 0
        a_abs = abs(a)
        b_abs = abs(b)
        while a_abs >= b_abs:
            a_abs = self.subtract(a_abs, b_abs)
            result = self.add(result, 1)
        if (a < 0) ^ (b < 0):
            result = -result
        return result
    
    def modulo(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot perform modulo by Zero")
        remainder = abs(a)
        b_abs = abs(b)
        while remainder >= b_abs:
            remainder = self.subtract(remainder, b_abs)
        return remainder if a >= 0 else -remainder

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition:", calc.add(1, 2))
    print("Example: subtraction:", calc.subtract(4, 2))
    print("Example: multiplication:", calc.multiply(2, 3))
    print("Example: division:", calc.divide(10, 2))
    print("Example: modulo:", calc.modulo(10, 3))
