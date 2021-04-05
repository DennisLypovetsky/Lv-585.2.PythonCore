number = int(input("Enter number: "))

if number == 0:
    print(f"{number}! = 1")
elif number < 0:
    print("Factorial does not exist for negative numbers")
else:
    def factorial(number):
        i = 1
        while number > 1:
            i *= number
            number -= 1
        return i

print(f"{number}! = {factorial(number):,}")