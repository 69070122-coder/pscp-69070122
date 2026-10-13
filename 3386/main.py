'''main'''
m = int(input())
n = int(input())
lis_m = []
lis_n = []

for _ in range(m):
    lis_m.append(input())

for _ in range(n):
    lis_n.append(input())

same = []

for i in range(n):
    for j in range(m):
        if lis_n[i] == lis_m[j] and lis_n[i] not in same:
            same.append(lis_n[i])
            break

if len(same) == 0:
    print("Nope")
else:
    same.sort(reverse=True)
    for i in range(len(same)):
        print(same[i])
