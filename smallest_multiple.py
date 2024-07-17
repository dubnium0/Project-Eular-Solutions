# Calculation Using the greatest common divisor
# https://www.wikiwand.com/en/Greatest_common_divisor

import math

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def lcm_multiple(numbers):
    result = 1
    for number in numbers:
        result = lcm(result, number)
    return result

if __name__ == "__main__":
    numbers = range(1, 21)
    result = lcm_multiple(numbers)
    print(f"The smallest multiple of the numbers from 1 to 20 is: {result}")