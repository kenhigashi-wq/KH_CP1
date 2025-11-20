# KH, period 2, Flexible Calculator Assignment
def calculator(operation, *args):
    if len(args) == 0:
        return "No numbers provided."
    
    if operation == "sum":
        total = 0
        for num in args:
            total += num
        return total
    
    elif operation == "average":
        total = 0
        for num in args:
            total += num
        return total / len(args)
    
    elif operation == "max":
        maximum = args[0]
        for num in args:
            if num > maximum:
                maximum = num
        return maximum
    
    elif operation == "min":
        minimum = args[0]
        for num in args:
            if num < minimum:
                minimum = num
        return minimum
    
    elif operation == "product":
        total = 1
        for num in args:
            total *= num
        return total
    
    else:
        return "Invalid operation"

def get_numbers():
    nums = []
    while True:
        user = input("Number: ")
        if user.lower() == "done":
            break
        try:
            nums.append(float(user))
        except:
            print("That's not a number. Please enter a number or 'done'.")
    return nums

def numbers_to_string(numbers):
    s = ""
    for i in range(len(numbers)):
        n = numbers[i]
        if n == int(n):
            s += str(int(n))
        else:
            s += str(n)
        if i != len(numbers) - 1:
            s += ", "
    return s

def main():
    print("Welcome to the Flexible Calculator!\n")
    print("Available operations: sum, average, max, min, product\n")
    
    while True:
        op = input("Which operation would you like to perform? ").strip().lower()
        while op not in ["sum", "average", "max", "min", "product"]:
            print("Invalid operation. Please choose one of: sum, average, max, min, product")
            op = input("Which operation would you like to perform? ").strip().lower()
        
        print("\nEnter numbers (type 'done' when finished):")
        nums = get_numbers()
        
        if len(nums) == 0:
            print("\nNo numbers entered. Nothing to calculate.\n")
        else:
            print("\nCalculating", op, "of:", numbers_to_string(nums))
            result = calculator(op, *nums)
            if isinstance(result, str):
                print("Result:", result)
            else:
                if result == int(result):
                    print("Result:", int(result))
                else:
                    print("Result:", result)
            print()
        
        again = input("Would you like to perform another calculation? (yes/no) ").strip().lower()
        if again != "yes":
            break
        print()
    
    print("\nThank you for using the Flexible Calculator!")

if __name__ == "__main__":
    main()