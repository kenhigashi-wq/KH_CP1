# KH 2nd basic calculator

#Remember to put our 1st line comment (initials, class period, assignment name)
#You will need 2 different inputs
#Convert to correct data types to run equations
#Your output needs to include the written equation and the result
#All floats need to be rounded to 2 decimal places
#Make sure your code works (test it 5 times with different numbers AND have your elbow partner test it!)
#Save your work
#Commit and push your code to Github
#Write a program that takes in two numbers and runs all of your basic math equations on those two numbers. 
# round all floats to 2 decimal places.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
answer = (input("Enter the operation (+, -, *, /, **, %, //): "))
if answer == "+":
    print(f"{num1} + {num2} = {float(num1 + num2, 2)}")
elif answer == "-":
    print(f"{num1} - {num2} = {float(num1 - num2, 2)}")
elif answer == "*":
    print(f"{num1} * {num2} = {float(num1 * num2, 2)}")
elif answer == "/":
    print(f"{num1} / {num2} = {float(num1 / num2, 2)}")
elif answer == "**":
    print(f"{num1} ** {num2} = {float(num1 ** num2, 2)}")
elif answer == "%":
    print(f"{num1} % {num2} = {float(num1 % num2, 2)}")
elif answer == "//":
    print(f"{num1} // {num2} = {float(num1 // num2, 2)}")