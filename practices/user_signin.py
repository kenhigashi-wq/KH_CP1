# KH 2nd user singnin practice

username = input("what is your user name: ")
password = input("what is your password: ")

setusername = "kensei"
setpassword = "123"

# The username stuff
if username == setusername:
    print(f"Welcome {username}!")
else: 
    print("You didn't succesfully sign in") # else wrong
if password == setpassword:
    print(f"your password is correct")
else:
    print("You didn't succesfully sign in") # else wrong