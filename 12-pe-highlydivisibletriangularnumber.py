run = True

master = []

start = 5000000


while run:
    master = []
    start+=1
    if len(master) >=499:
        run = False

    for div in range(start):
        try:
            if start % (div) == 0:
                master.append(div)
                # master.append(start)
        except ZeroDivisionError:
            pass


print(start)
