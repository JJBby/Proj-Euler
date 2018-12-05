# largest 2 digit palindrome is 9009 as a product of 91 X 99. Find largest of 3 digits

def palindrome(number):
    
    palindrome = 0
    large = 9009
  
    while True:
        left = number+1
        right= number+1
        for i in range(left-10, left):
            for j in range(right-10, right):
                large = i * j
                if str(large) == str(large)[::-1]:
                    if large < palindrome:
                        palindrome = large
        
        if palindrome > 0:
            break
        
        if left == right:
            left -= 9
        if right > left:
            right-=9
        if left > right:
            left -=9
        
    return palindrome

print(palindrome(99))
# generator for 10 sets of 10 numbers