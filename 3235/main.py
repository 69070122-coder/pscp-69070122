'''fat rabbit'''
n = int(input())
kratuy = []
numnak = []
count = 0
for i in range (n):
    bunny,weight=input().split()
    weight = int(weight)
    kratuy.append(bunny)
    numnak.append(weight)

for i in range(len(kratuy)):
    if numnak[i] > 15:
        count += 1
i = numnak.index(max(numnak))

print(count)
print(kratuy[i])
