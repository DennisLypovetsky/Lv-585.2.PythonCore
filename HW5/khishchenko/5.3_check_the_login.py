# Task3. Write a script that checks the login that the user enters. 
# If the login is "First", then greet the users. If the login is
# different, send an error message. 
# (need to use loop while)

user_login = input("Enter your login: ")

while user_login != 0:
    if user_login == "First":
        print("Welcom to our community")
    else:
        print("Your login do not match")
    break
