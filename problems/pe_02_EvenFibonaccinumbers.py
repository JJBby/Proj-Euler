
temp = 0
f1 = 1
f2 = 0
count = 0

while True:
    fib = f1 + f2
    if fib > 4000000:
       break
    if fib % 2 == 0:
        count += fib

    temp = f1
    f1 = fib 
    f2 = temp


print(f'{f1}, {f2}, Answer = {count}')
