'''
Polycarp got an array of integers a[1…n] as a gift. Now he wants to perform a certain number of operations (possibly zero)
so that all elements of the array become the same (that is, to become a1=a2=⋯=an).

In one operation, he can take some indices in the array and increase the elements of the array at those indices by 1.
For example, let a=[4,2,1,6,2]. He can perform the following operation: select indices 1, 2, and 4 and increase elements
of the array in those indices by 1. As a result, in one operation, he can get a new state of the array a=[5,3,1,7,2].

What is the minimum number of operations it can take so that all elements of the array become equal to each other
(that is, to become a1=a2=⋯=an)?

Input
The first line of the input contains a single integer t (1≤t≤104)  — the number of test cases in the test.
The following are descriptions of the input test cases.
The first line of the description of each test case contains one integer n (1≤n≤50)  — the array a.
The second line of the description of each test case contains n integers a1,a2,…,an (1≤ai≤109)  — elements of the array
a.
Output
For each test case, print one integer  — the minimum number of operations to make all elements of the array a equal.
Example
'''

t = int(input())
operations_list = []
for i in range(t):

    n = int(input())
    nums_in_a = input().split(' ')
    a = [int(x) for x in nums_in_a]
    operations = max(a) - min(a)
    operations_list.append(operations)

for operation in operations_list:
    print(operation)




