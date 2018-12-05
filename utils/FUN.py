# Boolean on off switch

def switch():
    
    try:
        numb = int(input('Enter a number to continue, a letter to quit:  '))
    except ValueError:
        exit()
   
    on_off = False

    if numb % 2 == 0:
        on_off = not on_off

    if on_off == True:
        print(f'{numb} is even')
    if on_off == False:
        print(f'{numb} + is odd')
    
    switch()

if __name__ == "__main__":
    switch()