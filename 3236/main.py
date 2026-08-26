'''code'''
n = int(input())
code1 = input()
code2 = input()

wrong = 0

for i in range(n):
    if int(code1[i]) + int(code2[i]) != 9:
        wrong += 1

if wrong == 0:
    print("YES")
else:
    print("NO", wrong)
