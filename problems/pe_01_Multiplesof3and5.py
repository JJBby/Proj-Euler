# Complete

start = 1000
num = 1
multiples = []

for each in range(start-1):  
  if num % 3 ==0 or num % 5==0:
     multiples.append(num)
  num+=1

print(sum(multiples))

# 233168