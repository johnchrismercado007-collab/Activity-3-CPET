user_name = input("please enter your username: ")
password = input("please enter your password: ")

stored_user = "JOHN CHRIS"
stored_pass = "arvinpass"

if user_name == stored_user and password == stored_pass:
    print("Access granted")
else:
    print("Access denied!")