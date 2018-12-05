# COMPLETE

f1 =1
f2 =1
temp = 0
total = 0
start_stop = True
index = 0
while start_stop:
    
    x = len(str(total)) 
    if x >= 1000:
        start_stop = False
        break
    index += 1
    total = f1 + (f1-f2)
    temp = f1
    f1 = f1 + f2
    f2 = temp

print(f"""
total at: {total}
f1 at: {f1}
f2 at: {f2} 
index at: {index}
""")