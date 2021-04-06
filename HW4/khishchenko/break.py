# Check if the list contains odd numbers. (Hint: use the break statement) 


for value in range(101):
    if value % 2 == 1:
        if value % 2 == 0:
            break
        print(value, end=' ')