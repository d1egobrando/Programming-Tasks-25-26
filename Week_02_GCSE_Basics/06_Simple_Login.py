print("\nLOGIN ")

correct_username ="dan"
correct_password ="123"
password_re_try = 3

while password_re_try > 0:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == correct_username and password == correct_password:
        print("Welcome " + correct_username)
        break

    else:
        print("Invalid username or password")
        password_re_try -= 1
        print("Number of re-trys left:", password_re_try)
