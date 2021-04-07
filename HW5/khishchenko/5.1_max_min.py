# Create a list of integers that are entered from the terminal 
# and determine the maximum and minimum number among them. 

user_list = []
 
integers_list = int(input("Enter list of numbers: "))

for i in range(0,integers_list):
    elements = int(input())
    user_list.append(elements)
print("Your list is: ", user_list)

print("Maximum number in the list: ", max(user_list))
print("Minimum number in the list: ", min(user_list))