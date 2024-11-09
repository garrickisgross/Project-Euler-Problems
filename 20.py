# sum the digits of the product of 100!

import math

str_answer = str(math.factorial(100))

sum = 0
for i in str_answer:
    sum += int(i)

print("sum:", sum)