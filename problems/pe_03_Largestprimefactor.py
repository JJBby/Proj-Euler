# # TODO
# # The prime factors of 13195 are 5, 7, 13 and 29.


def full_prime(numb):

    switch = True
    prime = numb
    x = 2
    arrprime = []

    while switch:

        if x >= prime:
            switch = False

        check = prime % x 

        if check != 0:
            x+=1
        if check == 0:
            arrprime.append(x)
            prime = prime / x

    return arrprime

x = full_prime(100)
print(x)

# 10,005,267,823,679,723
# 10,05,267,823,679,723  