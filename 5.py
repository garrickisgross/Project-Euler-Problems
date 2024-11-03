# 2520 is the smallest number that can be divided by each of the numbers from  1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# ANSWER: 232792560

x = 0

while True:
    x += 20
    
    has_false = False
    
    for i in range(20, 1, -1):
        if x % i != 0:
            has_false = True
        
    if not has_false:
        print("Solution:", x)
        break
    

 