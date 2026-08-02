'''how many odd and how many even'''
num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
even = 0
odd = 0
if not num_1 % 2:
    even += 1
else:
    odd += 1

if not num_2 % 2:
    even += 1
else:
    odd += 1

if not num_3 % 2:
    even += 1
else:
    odd += 1
print(even)
print(odd)
