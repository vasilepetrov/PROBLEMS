"""You are given two arrays a and b both consisting of n positive (greater than zero) integers. You are also given an integer k.

In one move, you can choose two indices i and j (1≤i,j≤n) and swap ai and bj (i.e. ai becomes bj and vice versa). Note
that i and j can be equal or different (in particular, swap a2 with b2 or swap a3 and b9 both are acceptable moves).

Your task is to find the maximum possible sum you can obtain in the array a if you can do no more than (i.e. at most) k
such moves (swaps).

You have to answer t independent test cases.

Input
The first line of the input contains one integer t (1≤t≤200) — the number of test cases. Then t test cases follow.

The first line of the test case contains two integers n and k (1≤n≤30;0≤k≤n) — the number of elements in a and b and the
maximum number of moves you can do. The second line of the test case contains n integers a1,a2,…,an (1≤ai≤30), where ai
is the i-th element of a. The third line of the test case contains n integers b1,b2,…,bn (1≤bi≤30), where bi is the i-th element of b.

Output
For each test case, print the answer — the maximum possible sum you can obtain in the array a if you can do no more than
(i.e. at most) k swaps."""

t = int(input())
sums = []
for test in range(t):
    n, k = [int(x) for x in input().split(' ')]  # first line of the test case

    numbers_arr_one = input().split(' ')
    numbers_arr_two = input().split(' ')
    a = [int(num) for num in numbers_arr_one]
    b = [int(num) for num in numbers_arr_two]

    for i in range(k):
        min_num_a = min(a)
        max_num_b = max(b)
        if min_num_a < max_num_b:
            a[a.index(min_num_a)], b[b.index(max_num_b)] = b[b.index(max_num_b)], a[a.index(min_num_a)]
        else:
            break
    sums.append(sum(a))

for s in sums:
    print(s)


