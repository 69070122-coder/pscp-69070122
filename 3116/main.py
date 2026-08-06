'''freaking harrd to under stand password genarator'''
name = input()
#first step
first = name[0].upper()
last = name[-1].upper()
first_ascii = ord(first)
last_ascii = ord(last)
#second step
num = []
for i in range(10):
    if (i + 1) % 2 == 1:
        num.append(first_ascii + i)
    else:
        num.append(last_ascii - i)
#third step
length = len(name)
for i in range(10):
    num[i] %= length
    if num[i] > 9:
        num[i] %= 10
#fianl
for x in num[2:8]:
    print(x, end=" ")
