
start_num = 0
best_num = 0
best_max_length = 0

def get_next_Collatz_num(i: int) -> int:
    if i % 2 == 0:
        return i / 2
    else: 
        return (3 * i) + 1

for i in range(2, 1000001):
    arr = [i]

    while arr[-1] != 1:
        arr.append(get_next_Collatz_num(arr[-1]))
    
    
    if best_max_length < len(arr):
        best_num = i
        best_max_length = len(arr)
    

print("solution,", best_num, best_max_length)
    
    

