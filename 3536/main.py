'''is prime'''
n = int(input())
if n < 2:
    print("NO")
elif n == 2:
    print("YES")
elif n % 2 == 0:
    print("NO")
else:
    prime = True
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            prime = False
            break
    if prime:
        print("YES")
    else:
        print("NO")
