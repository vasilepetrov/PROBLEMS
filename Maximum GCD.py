t = int(input())
max_numbers = []
for i in range(t):
    max_gcd = 1
    n = int(input())
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            a = j
            b = i
            r = a % b
            while r:
                a = b
                b = r
                r = a % b
            if b > max_gcd:
                max_gcd = b
    max_numbers.append(max_gcd)


for num in max_numbers:
    print(num)
