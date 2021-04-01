# Поміняти між собою значення двох змінних, не використовуючи третьої змінної.

a = 678
b = "hello"

print("Our variables ", a, b)

a, b = b, a

print("Swithed variables ", a, b)