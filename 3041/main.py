'''check if num_1 can be devide by 0'''
num_1 = float(input())
num_2 = float(input())
if not num_2:
    print("no")
elif not num_1 % num_2:
    print("yes")
else:
    print("no")
