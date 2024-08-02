# 10001. asal sayıyı bulma 

prime_dict = []
n = 1

while n<1000:
    prime_dict.append([6*n-1, 6*n+1])
    n += 1

print(prime_dict)