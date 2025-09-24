# KH 2nd letter grade prcatice project

grade = float(input("What is your grade in percentage: "))

if grade >= 94:
    print(f"Your grade is an A or {grade:.2f}%")
elif grade >= 90:
    print(f"Your letter grade is an A- or {grade:.2f}%")
elif grade >= 87:
    print(f"Your letter grade is a B+ or {grade:.2f}%")
elif grade >= 84:
    print(f"Your letter grade is a B or {grade:.2f}%")
elif grade >= 80:
    print(f"Your letter grade is a B- or {grade:.2f}%")
elif grade >= 77:
    print(f"Your letter grade is a C+ or {grade:.2f}%")
elif grade >= 74:
    print(f"Your letter grade is a C or {grade:.2f}%")
elif grade >= 70:
    print(f"Your letter grade is a C- or {grade:.2f}%")
elif grade >= 67:
    print(f"Your letter grade is a D+ or {grade:.2f}%")
elif grade >= 64:
    print(f"Your letter grade is a D or {grade:.2f}%")
elif grade >= 60:
    print(f"Your letter grade is a D- or {grade:.2f}%")
elif grade >= 0:
    print(f"Your letter grade is an F or {grade:.2f}%")
else:
    print("Thats not supposed tp happen. Try to type in a number")