'''this module for finding max number without using max() function'''
X = int(input())
Y = int(input())
Z = int(input())

max_num = X
if max_num <= Y:
    max_num = Y
else:
    pass

if max_num <= Z:
    max_num = Z
else:
    pass
print(max_num)
