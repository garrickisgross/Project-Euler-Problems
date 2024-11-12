#Evaluate the sum of all the amicable numbers under 10000

# d(n) is the sum of all proper divisors n
# d(a) = b and d(b) = a and a != b indicates numbers are amicable.

import math 

def sum_divisors(num: int) -> int:
    result = 0
     
    i = 2
    while i<= (math.sqrt(num)) :
        if (num % i == 0) :
            if (i == (num / i)) :
                result = result + i
            else :
                result = result +  (i + num/i)
        i = i + 1
    return int(result + 1)

def is_amicable(x: int, y: int) -> bool:
    if x != y:
        return sum_divisors(x) == y and sum_divisors(y) == x
    return False

sum = 0
for a in range(1, 10001):
    b = sum_divisors(a)
    if a == sum_divisors(b) and a != b:
        sum += a           

print(sum)








