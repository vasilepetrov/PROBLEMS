t = int(input())
numbers_to_check = [int(input()) for i in range(t)]
max_num = max(numbers_to_check)
powers_of_two = [2, ]
powers_of_two_initial = 2
power = 2
final = []
while powers_of_two_initial < max_num:
    powers_of_two.append(2 ** power)
    powers_of_two_initial = powers_of_two[-1]
    power += 1

for num in numbers_to_check:
    if num in powers_of_two:
        final.append('NO')
    else:
        final.append('YES')


for word in final:
    print(word)



