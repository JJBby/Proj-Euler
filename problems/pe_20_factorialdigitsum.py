# TODO!!!

import math


x = int(input('Enter number to be factored: '))
print(f'Factoring number: {x}')
y = math.factorial(x)

strings  = [int(d) for d in str(y)]

print('Factorial equals: ' + str(y))

total = (sum(strings))

print(f'Sum of each number in factorial: {total}')
