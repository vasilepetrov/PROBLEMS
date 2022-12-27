t = int(input())
participants_in_front = []
for i in range(t):
    numbers = input().split(' ')
    a, b, c, d = [int(x) for x in numbers]

    participants_in_front_of_Timur = [int(x) for x in numbers if int(x) > a]
    participants_in_front.append(len(participants_in_front_of_Timur))

for p in participants_in_front:
    print(p)