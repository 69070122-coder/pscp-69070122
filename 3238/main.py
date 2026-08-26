'''ion musk'''
x, k = input().split()
x = int(x)
for i in range(x):
    for j in range(x):
        if j == i or j + i == x - 1:
            if k == "#":
                print("#", end="")
            else:
                distance = abs(i - x // 2)
                print(chr(ord(k) + distance), end="")
        else:
            print("-", end="")
    print()
