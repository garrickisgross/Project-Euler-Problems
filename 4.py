# A palindromic number reads the same both ways. The largest palindrome made from the product of two-digit numbers is
# 9009 = 91 * 99
# Find the largest palindrome made from the product of two 3-digit numbers.
#ANSWER: 913 * 993 = 906609

def check_palindrome(x: int) -> bool:
    # cant iter through int, so convert to string, push to array, in python we can test equality with str
    i = str(x)
    arr = []
    for each in i:
        arr.append(each)
    split = len(arr)//2
    arr_a = arr[split:]
    arr_b = arr[:split]
    arr_b.reverse()
    if len(arr) % 2 == 0:
        return arr_a == arr_b
    else: 
        arr_a.pop(0)
        return arr_a == arr_b

max_prod = 0
for i in range(1000):
    for j in range(1000):
        if check_palindrome(i*j):
            if max_prod < i*j:
                max_prod = i*j
                print(i)
                print(j)

print(max_prod)
