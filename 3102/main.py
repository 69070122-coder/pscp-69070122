'''car tax'''
year = int(input())
CC = int(input())
if year <= 1990:
    if CC <= 1500:
        print(1250)
    elif 1501 <= CC <= 2000:
        print(1400)
    else:
        print(2000)
elif 1991 <= year <= 1999:
    if CC <= 1500:
        print(1100)
    elif 1501 <= CC <= 2000:
        print(1300)
    else:
        print(1700)
else:
    if CC <= 1500:
        print(1000)
    elif 1501 <= CC <= 2000:
        print(1200)
    else:
        print(1500)
