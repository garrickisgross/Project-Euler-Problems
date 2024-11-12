from math import sqrt 


def sum_divisors(num: int) -> int:
    """Return the sum of proper divisors of a number"""
    result = 0
     
    i = 2
    while i<= (sqrt(num)) :
        if (num % i == 0) :
            if (i == (num / i)) :
                result = result + i
            else :
                result = result +  (i + num/i)
        i = i + 1
    return int(result + 1)

def abundant(num: int) -> set:
    """Return all abundant numbers between 1 and that number. """
    s = set()
    for i in range(2, num + 1):
        if sum_divisors(i) > i:
            s.add(i)
    return s

magic_number = 28123

abundants = abundant(magic_number)

def is_sum_of_abundants(x: int) -> bool:
    
    for each in abundants:
        if x < each:
            break
        y = x - each
        if y in abundants:
            return True
    return False

# def is_sum_of_abundants(x: int) -> bool:
#     flag = False
#     for i in range(1, x):
#         y = x - i
#         if i in abundants and y in abundants:
#             flag = True
#             break
#     return flag
    
sum = 0

for i in range(1, magic_number + 1):
    if not is_sum_of_abundants(i):
        sum += i

print(sum)
