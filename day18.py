import math

def count_divisors(N):
    total = 0
    for i in range(1, int(math.isqrt(N)) + 1):
        if N % i == 0:
            total += 1 if i * i == N else 2
    return total

print(count_divisors(12))   
print(count_divisors(18))   
print(count_divisors(29))   
print(count_divisors(100))  
print(count_divisors(1))    
print(count_divisors(997))  
