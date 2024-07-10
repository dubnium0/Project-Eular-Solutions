def three_and_five_multiples(limit):
    sum_ = 0
    for n in range(1,limit+1):
        if n % 3 == 0 or n % 5 == 0:
            sum_ += n 
        else: 
            continue 
    return sum_

limit = 1000
a = three_and_five_multiples(1000)
print(a)