'''this module is for calculate how many time i press the calculator.'''
n = int(input())
amount = n

digits = 1
start = 1

if n == 1:
    print(1)
else:
    while start <= n:
        end = min(n, start * 10 - 1)
        amount += (end - start + 1) * digits
        start *= 10
        digits += 1
    print(amount)
