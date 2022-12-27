t = int(input())
max_numbers = []
for i in range(t):
    max_gcd = 1
    n = int(input())
    if n % 2 == 0:
        max_numbers.append(int(n / 2))
    else:
        max_numbers.append(int((n-1) / 2))

for num in max_numbers:
    print(num)