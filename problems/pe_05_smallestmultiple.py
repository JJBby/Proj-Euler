
def brute_force():

    y = 2520

    while True:
        mods = [y%x for x in (list(range(2, 21)))]
        remainders = sum(mods)
        if remainders == 0:
            break
        y += 2
    return y

print(brute_force())