# The sum of the squares of the first ten natural numbers is 385
# The square of the sum of the first ten natural numbers is 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
# ANSWER: 25164150 // This one felt too easy

sum_of_squares = 0
square_of_sum = 0
sum = 0

for i in range(1, 101):
    sum += i
    sum_of_squares += i * i

square_of_sum = sum * sum

print(square_of_sum - sum_of_squares)