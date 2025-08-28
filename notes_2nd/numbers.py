# VL 2nd Integers and Floats Notes

# Integers
# Integers are whole numbers, both positive and negative, including zero.
a = 10        # positive integer
b = -5        # negative integer    
c = 0         # zero

#Floats(floating point numbers)
# Floats are numbers that have a decimal point.
x = 3.14      # positive float  
y = -2.71     # negative float
z = 0.0       # zero as a float

# Arithmetic Operations
sum_result = a + b          # Addition
diff_result = a - b         # Subtraction
prod_result = a * b         # Multiplication
div_result = a / 2          # Division (results in float)
int_div_result = a // 3     # Integer Division (results in integer, whole number from division)
mod_result = a % 3          # Modulus (remainder, whole #)
exp_result = a ** 2         # Exponentiation

#math
print(8/4 +7-(8+2)%4**2)  # PEMDAS
# How do we calcualte exponents in python?
print(2**3)  # 2^3 = 2*2*2 = 8  
# Change data types
age = int(input("How old are you?\n"))
int_to_float = float(a)    # Convert integer to float
print("wow you are old", 5256000*age, "minutes old") # 525600 minutes in a year

brain_cells = float(input("how many brain cells you have"))
print("are you sure you have", brain_cells/2, "brain cells left")

#rounding
pi = 3.1423489
print(round(pi, 4))  # Round to 4 decimal places

# How do you change data to a float?
int_to_float = float(a)    # Convert integer to float
# How do you change data to an integer?
float_to_int = int(x)      # Convert float to integer (truncates decimal part)