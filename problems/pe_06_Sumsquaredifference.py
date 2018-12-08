natural = 0
added =0


for num in range(101):
    natural += num**2
    added += num

square = added**2
            
print(f'Natural: {natural} \nSquare: {square} \nDifference of square - natural is: {square- natural}')