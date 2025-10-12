# KH, period , password checker 

# Ask the user for a password
password = input("Enter a password: ")

# Start score at 0
score = 0

# Check if password is at least 8 characters
if len(password) >= 8:
    print("Length (8+ characters): Yes")
    score += 1
else:
    print("Length (8+ characters): No")

# Check for uppercase letters
upper = False
for letter in password:
    if letter >= 'A' and letter <= 'Z':
        upper = True
if upper:
    print("Contains uppercase: Yes")
    score += 1
else:
    print("Contains uppercase: No")

# Check for lowercase letters
lower = False
for letter in password:
    if letter >= 'a' and letter <= 'z':
        lower = True
if lower:
    print("Contains lowercase: Yes")
    score += 1
else:
    print("Contains lowercase: No")

# Check for numbers
has_number = False
for letter in password:
    if letter >= '0' and letter <= '9':
        has_number = True
if has_number:
    print("Contains numbers: Yes")
    score += 1
else:
    print("Contains numbers: No")

# Check for special characters
special = "!@#$%^&*()_+-=[]{}|;:,.<>?"
has_special = False
for letter in password:
    if letter in special:
        has_special = True
if has_special:
    print("Contains special characters: Yes")
    score += 1
else:
    print("Contains special characters: No")

# Show score
print()
print("Strength score:", score, "/ 5")

# Give feedback
if score <= 2:
    print("Password strength: Weak")
elif score == 3:
    print("Password strength: Moderate")
elif score == 4:
    print("Password strength: Strong")
elif score == 5:
    print("Password strength: Very Strong")