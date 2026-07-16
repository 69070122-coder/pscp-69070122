"""67"""
x = int(input())
y = int(input())
if not x and not y:
    print("O")
elif not x and y:
    print("Y")
elif x and not y:
    print("X")
elif x >= 1 and y >= 1:
    print("Q1")
elif x <= 1 and y >= 1:
    print("Q2")
elif x <= 1 and y <= 1:
    print("Q3")
else:
    print("Q4")
