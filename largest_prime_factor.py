def largest_prime_factor(n):
    
    largest_factor = 2
    
    for i in range(3, int(n**0.5)):
        while n % i == 0:
            largest_factor = i
            n = n // i

    if n > 2:
        largest_factor = n
    
    return largest_factor

if __name__ == "__main__":
    number = 600851475143
    result = largest_prime_factor(number)
    print(f"The largest prime factor of {number} is: {result}")