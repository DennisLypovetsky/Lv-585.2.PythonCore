# Print Fibonacci numbers up to the entered number n, using cycles. 
# (Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.) 

number = int(input('Enter positive number: '))

start_number = 0
count = 1
fibo_number = number

while start_number < number:
    print(start_number)
    start_number = start_number + count
    if start_number > fibo_number:
            break
    print(count)
    count = count + start_number