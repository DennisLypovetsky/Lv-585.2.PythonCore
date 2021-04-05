# Write a script, which of the two entered 
# numbers will determine which of them is
# more and which is less. Take into account 
# the case of equality of numbers. 


a = int(input('Enter number a: '))
b = int(input('Enter number b: '))

# a = 52
# b = 50

if a > b:
    print('Number a more then number b')
elif a < b:
    print('Number b more then number a')
elif a == b:
    print('Numbers are equal')
