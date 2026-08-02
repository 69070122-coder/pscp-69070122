'''easy roman'''
roman = ["I","II","III","IV","V","VI","VII","VIII","IX","Error : Please input positive number"]
num = int(input())
if 1 <= num <= 9:
    print(roman[num-1])
elif num > 9 or not num:
    print("Error : Out of range")
else:
    print(roman[9])
