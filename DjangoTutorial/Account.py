print("Register an account")
username=input("Enter your username: ")
password=input("Enter your password: ")
print("Your account has been created successfully")

print("Login to your account")
username2=input("Enter your username: ")
password2=input("Enter your password: ")

if username==username2 and password==password2:
    print("You have logged in successfully")
else:
    print("Invalid username or password")