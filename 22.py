import string
names = ""

with open("assets/names.txt", 'r') as f:
    names = f.readlines()[0].replace('"',"").replace(" ", "").split(',')
    f.close()

names.sort()

sum = 0

for i in range(len(names)):
    n = i + 1
    name = names[i]
    local = 0
    for char in name:
        x = string.ascii_lowercase.index(char.lower()) + 1
        local += x
    sum += int(local * n)

print(sum)


