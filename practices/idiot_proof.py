# KH 2nd idiot proof
name = input("What is your name? ").strip().title()
phone = input("What is your phone number? ").strip()
phone = " ".join([phone[:-4][i:i+3] for i in range(0, len(phone) - 4, 3)]) + " " + phone[-4:]
gpa = float(input("What is your GPA?: "))

print(name, phone, gpa)