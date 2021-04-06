# Print all even numbers less than 100 (write two variants of the code: 
# one using the while loop, and the other using the for loop). 

# While loop

value = 0

while value < 100:
    value += 2
    print(value, end=" ",)
    
print('\n')

# For loop

for i in range(101):
    if i % 2 == 0:
        print(i, end=" ")
        