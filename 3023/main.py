'''this module is for calculate how many time i press the calculator.'''
n = int(input())
amount = 1
if n == 1:
    print(f"{amount}")
else:
    for i in range(n-1):
        amount += len(str(i + 2))
    amount += (n)
    print(amount)
