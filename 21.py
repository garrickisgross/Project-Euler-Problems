#Evaluate the sum of all the amicable numbers under 10000

# d(n) is the sum of all proper divisors n
# d(a) = b and d(b) = a and a != b indicates numbers are amicable.

def sum_divisors(x: int) -> int:
    sum = 0

    for i in range(1, x):
        if x % i == 0:
            sum += i
    return sum

def is_amicable(x: int, y: int) -> bool:
    return sum_divisors(x) == sum_divisors(y)





amicable = []
temp = []

def main():
    sum = 0
    for i in range(1, 10001):
        
        sum_div = sum_divisors(i)
        found = False
        
        if [i, sum_div] not in temp:
            pass
        
        if not found:
            pass

    for key in temp.keys():
        if len(temp[key]) > 1:
            for i in temp[key]:
                amicable.append(i)

    for i in amicable:
        sum += i
    return sum


print(main())







