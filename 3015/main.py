"""promotion eiei"""
x = int(input())
y = int(input())
a = int(input())
z = int(input())
fullGroup = z//x
remainder = z % x
print((fullGroup * y + remainder) * a)
