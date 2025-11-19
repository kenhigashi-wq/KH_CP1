# KH, period 2, Flexible Calculator Assignment

import statistics

# Function to perform calculation based on operation
def flexible_calculator(*args, operation='sum'):
    # Check if numbers are provided
    if not args:
        return "No numbers provided."
    
    # Perform operation based on user choice
    if operation == 'sum':  # Calculate sum of all numbers
        return sum(args)
    elif operation == 'average':  # Calculate average using statistics.mean
        return statistics.mean(args)
    elif operation == 'max':  # Find maximum value/
        return max(args)
    elif operation == 'min':  # Find minimum value
        return min(args)
    elif operation == 'product':  # Multiply all numbers together
        product = 1
        for num in args:
            product *= num
        return product
    else:  # Handle invalid operation
        return "Invalid operation."

# Main function for user 'interface
def main():
    print("Welcome to the Flexible Calculator!\n")
    print("Available operations: sum, average, max, min, product\n")
    
    while True:  # Loop until user chooses to exit
        operation = input("Which operation would you like to perform? ").strip().lower()
        
        # Validate operation input
        if operation not in ['sum', 'average', 'max', 'min', 'product']:
            print("Invalid operation. Please try again.\n")
            continue
        
        numbers = []  # List to store user inputs
        print("\nEnter numbers (type 'done' when finished):")
        
        # Collect numbers until user types 'done'
        while True:
            user_input = input("Number: ").strip().lower()
            if user_input == 'done':  # Stop collecting numbers
                break
            try:
                num = float(user_input)  # Convert input to float
                numbers.append(num)
            except ValueError:  # Handle invalid numeric input
                print("Invalid input. Please enter a number or 'done'.")
        
        # Display calculation result if numbers exist
        if numbers:
            print(f"\nCalculating {operation} of: {', '.join(map(str, numbers))}")
            result = flexible_calculator(*numbers, operation=operation)  # Call calculator function
            print(f"Result: {result}\n")
        else:
            print("No numbers entered. Cannot calculate.\n")
        
        # Ask user if they want another calculation
        again = input("Would you like to perform another calculation? (yes/no) ").strip().lower()
        if again != 'yes':  # Exit loop if user says no
            print("\nThank you for using the Flexible Calculator!")
            break

# Run the program
if __name__ == "__main__":
    main()
