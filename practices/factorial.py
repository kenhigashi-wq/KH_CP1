#KH psuedocode practice

#Ask the user for a number
#Check what the user typed in is a number
#(ken version) Make a function for checking it
#(k) make empty list
#(k)Make a try to check if its integer
#(k)Except, ValueError
#(k)If get numbers(num), print "Valid"
#(k)else, print (nvalid)
# #And if not ask again
# #Take the number and see what numbers are smaller then it makes it stop at one.
#make a function that takes the number user put in and multiply it with the numbers
#print output and input at same time
#(ken version)Make an empty list for the numbers
#call for function



def get_numbers(num):
    try:
            int(num)
            return True
    except ValueError:
        
        return False
    
num = input("Enter a number: ")    

if get_numbers(num):
     print(f"{num} is valid")
else:
     print(f"{num} is not valid")

