'''your BONUS issssss'''
position,year,salary = input().split()
year = int(year)
salary = int(salary)
bonus = 0
if position == "M":
    if year < 5:
        bonus = 1500 + salary * 0.06
    elif year <= 10:
        bonus = 1500 + salary * 0.08
    else:
        bonus = 1500 + salary * 0.10

elif position == "B":
    if year < 5:
        bonus = 1000 + salary * 0.05
    elif year <= 10:
        bonus = 1000 + salary * 0.06
    else:
        bonus = 1000 + salary * 0.07

elif position == "G":
    if year < 5:
        bonus = 500 + salary * 0.04
    elif year <= 10:
        bonus = 500 + salary * 0.05
    else:
        bonus = 500 + salary * 0.06

print(int(bonus))
