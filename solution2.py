def sum_even_fibonacci_number():
    limit = 4000000
    a, b = 1,2
    sum_even = 0
    while a<=limit:
        if a%2 ==0:
            sum_even+=a
        a, b = b, a+b
    return sum_even
    
if __name__ == "__main__":
    a = sum_even_fibonacci_number()
    print(a)