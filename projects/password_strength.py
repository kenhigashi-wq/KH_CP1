# KH password strentgh checker project



#Define the integer. (:
num = "1","2","3","4","5","6","7","8","9","0"
#Define the special character
spec = "!","@","#","$","%","^","&","*","(",")","_","+","-","=","[","]","{","}","|",";",":",".","<",">","?"
#define the upper case
lower = "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
#define uppercase
upper = "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"


# Add a while true loop
while True:
# Add a password strength score
    score = 0 
# Add password input
    password = input("Input your password")
# Check for the length
    if len(password) >= 8:
#add score
        score += 1
#check for the number
    if num(password) >= 1:
#add score
        score += 1
#check for special letters
    if spec(password) >= 1:
#add score
        score += 1
#check for lower case
    if lower(password) >= 1:
#add score
        score += 1
# check for upper case
    if upper(password) >= 1:
#add score
        score += 1
    print(f"your score is {password}")