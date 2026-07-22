"""this module is to find the lowest number
 from input without using min()"""
amount = int(input())
num = []
for i in range(amount):
    number = int(input())
    num.append(number)
min_num = num[0]
for i in num:
    if i < min_num:
        min_num = i

print(min_num)
