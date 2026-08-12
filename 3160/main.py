'''is prime'''
start,end = map(int,input().split())
prime = []

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if not num % i:
                break
        else:
            prime.append(num)

if prime:
    print(*prime)
print(f"Total primes: {len(prime)}")
