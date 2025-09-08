# KH 2nd Format Output Notes

name = "John Doe"
age = 30
grade = 0.85
money = 250.5

print("hello {}, nice to meet you! You are {:b} years old. You have a {:%} in this class, you have $ {:.2f}, that is a lot of money".format(name,
age, grade, money))

print(f"hello {name}, nice to meet you! You are {age:b} years old. You have a {grade:%} in this class, you have $ {money:.2f}, that is a lot of money")