#Evaluate the sum of all the amicable numbers under 10000

# d(n) is the sum of all proper divisors n
# d(a) = b and d(b) = a and a != b indicates numbers are amicable.

import math 

def sum_divisors(num: int) -> int:
    # Final result of summation of divisors
    result = 0
     
    # find all divisors which divides 'num'
    i = 2
    while i<= (math.sqrt(num)) :
       
        # if 'i' is divisor of 'num'
        if (num % i == 0) :
       
            # if both divisors are same then
            # add it only once else add both
            if (i == (num / i)) :
                result = result + i
            else :
                result = result +  (i + num/i)
        i = i + 1
         
    # Add 1 to the result as 1 is also 
    # a divisor
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








