
import math


def generate_tri_number(i: int) -> int:
    sum = 0
    for x in range(1, i + 1):
        sum += x
    return sum

# a divisor counter algo with O(sqrt(n)) complexity pulled from wikipedia, z does different things, we need 0 here
def count_divisors(n, z = 0):
    sum = 0
    for d in range(1, int(math.sqrt(n)) + 1):
        if n % d == 0:
            sum += d ** z 
            if d != n // d: 
                sum += (n // d) ** z
    return sum

divisor_count = 0
tri_idx = 0
tri_num = 0

while divisor_count < 500:
    
    tri_idx += 1
    tri_num = generate_tri_number(tri_idx)
    div = count_divisors(tri_num)
    
    if divisor_count < div:
        divisor_count = div
    

print(tri_num, f"is the {tri_idx} tri-number, it has {divisor_count} divisors")


