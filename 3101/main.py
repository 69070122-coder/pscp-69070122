'''water state in any temp'''
temp = int(input())
unit = input().lower()

if unit == "f":
    temp = (temp - 32) * 1.8

if temp <= 0:
    print("solid")
elif temp >= 100:
    print("gas")
else:
    print("liquid")
