# A Pythagorean triplet is a set of three natural numbers, a < b < c for which a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
# There exists exactly one Pythagorean triplet for which a + b + c = 1000
# Find the product abc
# ANSWER: 31875000
# Triplet: 200, 375, 425


def check_pythag(a: int, b: int, c: int) -> bool:
    return a*a + b*b == c*c

solved = False

for i in range(1, 1000):

    for j in range(1, 1000):
        
        for z in range(1, 1000):

            if check_pythag(i,j,z) and i + j + z == 1000 and i < j and j < z:
                print("Solution:", i*j*z)
                print("Triplet=", i, j, z)
                solved = True
            if solved: 
                break
        if solved:
            break
    if solved:
        break
            
