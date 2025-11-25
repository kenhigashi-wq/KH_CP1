#KH psuedocode practice

#Check what the user typed in is a number
#(ken version) Make a function for checking it
#(k) make empty list
#(k)Make a try to check if its integer
#(k)Except, ValueError
#Ask the user for a number
#(k)If get numbers(num), print "Valid"
#(k)else, print (invalid)
# #And if not ask again
#(k)make function for calculating the factorial stuff
#(k)Set result to 1
#(K)Loop throuh every num from 1 up to n
#result = result * i or result *= i
#return output
#print output and input at same time(?)
#(ken version)Make an empty list for the numbers
#(k)Make output var with factorial(num)
#Print factorial


def get_numbers(num):
    try:
            int(num)
            return True
    except ValueError:
     print("False please try again")
     return False
    
num = input("Enter a number: ")

if get_numbers(num):
     print(f"{num} is a valid integer")
     num = int(num)
else:
     print(f"{num} is not valid")
     exit()

def factorial(n):
     result = 1
     for i in range(1, n + 1):
          result *= i
     return result

if num < 0:
     print("invalid, please try again with a positive number.")
else:
     print("Input is a vaild, positive number")
output = factorial(num)
print(f"The factorial is:{output}")