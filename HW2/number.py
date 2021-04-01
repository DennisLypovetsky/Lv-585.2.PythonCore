# Задано чотирицифрове натуральне число. 

natural_number = str(1580)

print("Natural number ", natural_number)

# Знайти добуток цифр цього числа.

print("Sum of elements in number ", eval("1 + 5 + 8 + 0"))

# Записати число в реверсному порядку.

list_natural_number = list(natural_number)
list_natural_number.reverse()
reverse_natural_number = "".join(list_natural_number)
print("Reversed number ", reverse_natural_number)

# Посортувати цифри, що входять в дане число.

numbers = [1, 5, 8, 0]
numbers.sort()
print("Sort of number ", numbers)