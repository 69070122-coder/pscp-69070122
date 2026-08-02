'''ticket price'''
age,day = map(str,input().split())
A = int(age)
if A < 5:
    PRICE = 0
elif 5 <= A <= 18:
    PRICE = 100
else:
    PRICE = 150

if day == "Wed":
    print(f"{PRICE/2:.0f}")
else:
    print(f"{PRICE:.0f}")
