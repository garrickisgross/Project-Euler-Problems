# how many sundays fell on the first of the month from january 1st 1901 to december 31st 2000


import datetime


count = 0

for year in range(1901, 2001):
    for month in range(1, 13):
        if datetime.date(year, month, 1).isoweekday() == 7:
            count += 1 

print(count)