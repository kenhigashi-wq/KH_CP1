# KH 2nd Elif and logical operators notes

homework = True
chores = True
room = False

if homework and chores and room:
    print("You can go to your friends house.")
elif not chores or not room:
    print("Do your chores!")
else:
    print("Go do your homework")

username = input("Enter your username")
password = input("Enter your password")

if username == "ken" and password == "123":
    print("welcome ken!")
elif username == "Tia" and password == "pass":
    print("welcome tia")
else:
    print("Not valid")