'''this module for finding min number without using min() function'''
X = int(input())
Y = int(input())
Z = int(input())

min_num = X
if min_num >= Y:
    min_num = Y
else:
    pass

if min_num >= Z:
    min_num = Z
else:
    pass
print(min_num)
