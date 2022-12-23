'''
Vasily the Programmer loves romance, so this year he decided to illuminate his room with candles.

Vasily has a candles.When Vasily lights up a new candle, it first burns for an hour and then it goes out. Vasily is smart,
so he can make b went out candles into a new candle. As a result, this new candle can be used like any other new candle.

Now Vasily wonders: for how many hours can his candles light up the room if he acts optimally well? Help him find this
 number.

Input
The single line contains two integers, a and b (1 ≤ a ≤ 1000; 2 ≤ b ≤ 1000).

Output
Print a single integer — the number of hours Vasily can light up the room for.
'''

initial = input().split(' ')
initial_value_a = int(initial[0])
initial_value_b = int(initial[1])
a, b = [int(x) for x in initial]
hours_burned = a // b * b

while a >= b:
    candles_that_can_be_made = a // b
    candles_that_will_remain = a % b
    a = candles_that_can_be_made + candles_that_will_remain
    hours_burned += (a // b) * b
hours_burned += a
print(hours_burned)
