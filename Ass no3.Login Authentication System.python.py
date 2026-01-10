username = "dd_admin"
password = "dd@2025"

user_input = input("Enter Username: ")
pass_input = input("Enter Password: ")

if user_input == username and pass_input == password:
    print("Login successful")
else:
    print("Access Denied")
