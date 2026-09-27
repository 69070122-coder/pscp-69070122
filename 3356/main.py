'''im bussing'''
n = int(input())
m = int(input())
x = int(input())

for i in range(n):
    row = []
    for j in range(m):
        number = n - i + j * n
        if number == x:
            row.append("XX")
        else:
            row.append(f"{number:02}")
    print(" ".join(row))
    if i % 2 == 1 and i != n - 1:
        print()
