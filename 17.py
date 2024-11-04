import inflect

e = inflect.engine()

arr = []
count = 0
for i in range(1, 1001):
    words = e.number_to_words(i)
    arr.append(words)


for i in arr:
    for x in i:
        if x == " ":
            continue
        if x == "-":
            continue
        count += 1
print(count)

