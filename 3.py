
x = 600851475143

def check_prime(i: int) -> bool: 
    if (i == 0 or i == 1 or i < 0):
        return False
    j = 2

    while j*j <= i:
        if i % j == 0:
            return False
        j += 1    
        
    return True

highest_prime = None
while True:
    if check_prime(x):
          highest_prime = x
          break
        
    for i in range(2, int(x)):
        if (x % i == 0):
            x = x / i
            break

print(highest_prime)