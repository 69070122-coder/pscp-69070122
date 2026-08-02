'''price pf the texi'''
KM = int(input())
if KM <= 0:
    print(0)
elif KM == 1:
    print(35)
elif 1 < KM <= 10:
    print(35 + 5*(KM - 1))
else:
    print(35 + 45 + (KM - 10)*8)
