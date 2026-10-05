'''coke v2'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if b == 0:
    answer = a * d
else:
    discounted = (d - 1) // b
    normal = d - discounted

    answer = normal * a + discounted * c
print(answer)
