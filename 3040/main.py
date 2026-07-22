'''this module is for calculating the amount of 10thb coin
5thb coin 2 thb coin and 1 thb coin'''
money = int(input())
amount_10 = 0
amount_5 = 0
amount_2 = 0
amount_1 = 0
if money >= 10:
    amount_10 = money//10
    money -= 10 * amount_10
if money >= 5:
    amount_5 = money // 5
    money -= 5 * amount_5
if money >= 2:
    amount_2 = money // 2
    money -= 2 * amount_2
if money >= 1:
    amount_1 = money // 1
    money -= 1 * amount_1
print(f"10 = {amount_10}")
print(f"5 = {amount_5}")
print(f"2 = {amount_2}")
print(f"1 = {amount_1}")
