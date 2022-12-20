'''
Problem 1360A CodeForces
'''

t = int(input())
side_square = 0
square_sides = []
for i in range(t):
    a, b = [int(x) for x in input().split(' ')]
    if b > a:
        a, b = b, a

    if a == b:
        side_square = 2 * a

    elif a > 2 * b:
        side_square = a

    elif b <= a <= 2 * b:
        side_square = 2 * b
    square_sides.append(side_square)

for side in square_sides:
    print(side * side)
