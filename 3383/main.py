'''main'''
n = int(input())
m = int(input())

A = set()
B = set()

for _ in range(n):
    A.add(int(input()))

for _ in range(m):
    B.add(int(input()))

result = A - B

for x in result:
    print(x,end =" ")
