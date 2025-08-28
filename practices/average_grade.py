#KH 2nd average grade practice
# I will write a program that takes in grades for each of your classes and then outputs for the user their average grade (rounded to 2 decimal places).
print("Welcome to the average grade calculator!, please use numbers only, no % sign.")
one = float(input("What is your first period grade?\n"))     
two = float(input("What is your second period grade?\n"))
three = float(input("What is your third period grade?\n"))
four = float(input("What is your fourth period grade?\n"))
five = float(input("What is your fifth period grade?\n"))
six = float(input("What is your sixth period grade?\n"))
seven = float(input("What is your seventh period grade?\n"))

total = one + two + three + four + five + six + seven
average = total / 7
print("Your average grade is", round(average, 2),"percent.")
round(average, 2)
#round function rounds to the nearest whole number unless you specify the number of decimal places you want to round to.