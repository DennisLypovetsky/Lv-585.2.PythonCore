# Задано чотирицифрове натуральне число. 

natural_number = input("Enter natural number from 1000 to 9999: ")

# Знайти добуток цифр цього числа.
multiplication_natural_number = int(natural_number[0])*int(natural_number[1])*int(natural_number[2])*int(natural_number[3])
print("Multiplication of elements in number ", multiplication_natural_number)

# Записати число в реверсному порядку.

list_natural_number = list(natural_number)
list_natural_number.reverse()
reverse_natural_number = "".join(list_natural_number)
print("Reversed number ", reverse_natural_number)

# Посортувати цифри, що входять в дане число.

sort_natural_number = sorted(natural_number)
sorted_natural_number = "".join(sort_natural_number)
print("Sorted number ", sorted_natural_number)