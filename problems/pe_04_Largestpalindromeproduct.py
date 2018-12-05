# largest 2 digit palindrome is 9009 as a product of 91 X 99. Find largest of 3 digits

def palindrome(number):
    
    palindrome = 0
    large = 0
    num = number + 1

    for i in range(num):
        for j in range(num):

            large = i * j
            
            if str(large) == str(large)[::-1]:
                if large > palindrome:
                    palindrome = large
        
    return palindrome

print(palindrome(99))
# generator for 10 sets of 10 numbers