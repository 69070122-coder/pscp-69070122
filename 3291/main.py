'''right arrow'''
k = int(input())
n = int(input())
for i in range (n):
    space = n // 2 - abs(n // 2 - i)
    print(" "*space + "*"*k)
