# 1,000,000,000
primes =[2]
for num in range(3,10**9,2):
    # if len(primes) > 100000000: # 100,000,000
    #     break
    if all(num%i!=0 for i in range(3,int(num**.5)+1, 2)):
        primes.append(num)

# print(primes)
print(f'The { len(primes) }th prime is {primes[-1]}')

# count = 23
# primes=[1, 2, 3, 5, 7, 11, 13, 17, 19, 23]
# switch = True

# while switch:
#     if len(primes) >= 100:
#         switch = False
#         break

    

#     primes.append(x)

#     count +=2
