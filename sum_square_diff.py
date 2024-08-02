def sum_sq_diff(n):
    sum_sq = sum([i**2 for i in range(1, n+1)])
    sq_sum = sum([i for i in range(1, n+1)])**2
    return sq_sum - sum_sq

if __name__ == "__main__":
    n = 10
    result = sum_sq_diff(n)
    print(f"The difference between the sum of the squares of the first {n} natural numbers and the square of the sum is: {result}")