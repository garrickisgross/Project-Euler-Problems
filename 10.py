# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
# Find the sum of all the primes below two million.
# ANSWER: 142913828922

sum = 0

def check_prime(i: int) -> bool: 
    if (i == 0 or i == 1 or i < 0):
        return False
    j = 2

    while j*j <= i:
        if i % j == 0:
            return False
        j += 1    
        
    return True

for i in range(1, 2000000):
    if check_prime(i):
        sum += i

print(sum)