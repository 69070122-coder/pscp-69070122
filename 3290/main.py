'''left arrow'''
k = int(input())
n = int(input())

for i in range (n):
    space = abs(n // 2 - i)
    print(" "*space + "*"*k)
