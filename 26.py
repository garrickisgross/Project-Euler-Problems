num = 1
s = ''
max_len = (0,'')
for i in range(2, 1001):
    div = num/i
    str_div = str(div)
    str_div = str_div[2:]

    chars = []
    for j in str_div:
        if j not in chars:
            chars.append(j)

    s = ''.join(chars)
    if len(s) > max_len[0]:
        max_len = (i, s)
        

print(max_len)
