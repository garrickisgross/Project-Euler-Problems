# By listing the first six prime numbers: 2,3,5,11, and 13 we can see the 6th prime number is 13
# Find the 10,001th prime number
# ANSWER: 104743


count_of_primes = 0

def check_prime(i: int) -> bool: 
    if (i == 0 or i == 1 or i < 0):
        return False
    j = 2

    while j*j <= i:
        if i % j == 0:
            return False
        j += 1    
        
    return True

i = 2
while count_of_primes != 10001:
    if check_prime(i):
        count_of_primes += 1
        print(i, count_of_primes)
    i += 1