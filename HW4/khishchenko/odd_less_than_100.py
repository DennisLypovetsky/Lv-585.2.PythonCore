# Print all odd numbers less than 100. (write two versions of the code: 
# one using the continue operator, and the other without this operator). 

# Using the continue operator

for value in range(101):
    if value % 2 == 0:
        continue
    print(value, end=' ')

print('\n')

# Without the continue operator

for value in range(101):
    if value % 2 == 1:
        print(value, end=' ')
