'''giraffe'''
n = int(input())
giraffe = []
for i in range(n):
    giraffe.append(int(input()))
count = 0
for i in range(n):
    if i == 0:
        if n == 1 or giraffe[i] > giraffe[i + 1]:
            count += 1
    elif i == n - 1:
        if giraffe[i] > giraffe[i - 1]:
            count += 1
    else:
        if giraffe[i] > giraffe[i - 1] and giraffe[i] > giraffe[i + 1]:
            count += 1
print(count)
