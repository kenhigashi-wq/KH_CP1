# KH - 2nd Period - Order Up Practice Project

# Menu dictionary
menu = {
    'drink': {
        'Coke': 2.05,
        'Water': 2.05,
        'Fizzy Water': 5.00,
        'Mud': 100.05
    },
    'main course': {
        'Burger': 8.99,
        'Ribeye': 26.55,
        'Sirloin': 16.49,
        'BBQ Chicken Sandwich': 16.49
    },
    'side dishes': {
        'Fries': 3.99,
        'Salad': 4.50,
        'Baked Potato': 5.59,
        'Corn': 3.49
    }
}

# Display full menu
print("=== MENU ===")
for category, items in menu.items():
    print(f"\n{category.capitalize()}:")
    for item, price in items.items():
        print(f"  {item} - ${price:.2f}")

# Function to validate user input
def get_valid_choice(category, options):
    while True:
        choice = input(f"\nChoose your {category} ({', '.join(options)}): ").strip()
        if choice in options:
            return choice
        else:
            print("Invalid choice. Please try again.")

# Take order
def place_order():
    while True:
        print("\n=== Place Your Order ===")
drink = get_valid_choice("drink", menu['drink'].keys())
main_course = get_valid_choice("main course", menu['main course'].keys())


# Two side dishes
side1 = get_valid_choice("first side dish", menu['side dishes'].keys())
side2 = get_valid_choice("second side dish", menu['side dishes'].keys())

# Calculate total
total = (menu['drink'][drink] +
         menu['main course'][main_course] +
         menu['side dishes'][side1] +
         menu['side dishes'][side2])

# Display order 
print("\n=== Your Order ===")
print(f"Drink: {drink}")
print(f"Main Course: {main_course}")
print("Side Dishes:")
print(f"  {side1}")
print(f"  {side2}")
print(f"\nTotal Cost: ${total:.2f}")