# Write a function that returns the arithmetic mean
# of any number of numbers.

def arithmetic_mean(quantity, number_list):
    numbers_sum = sum(number_list)
    return numbers_sum / quantity

print(arithmetic_mean(7, [5,7,8,2,4,5,9]))
