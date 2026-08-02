'''just finding if the num input are the same'''
N = 3
all_num = []
for i in range (N):
    num = float(input())
    all_num.append(num)
    i += 0

if all_num[0]== all_num[1] == all_num[2]:
    print("all the same")
elif all_num[0] != all_num[1] != all_num[2] != all_num[0]:
    print("all different")
else:
    print("neither")
