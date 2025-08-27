import random

class Company:
    def __init__(self, name):
        self.name = name
        self.progress = 70
        self.profits = 100_000_000
        self.expenses = 60_000_000
        self.stock_price = 180.0
        self.new_products = 2

    def take_action(self, action):
        if action == "invest":
            self.profits -= 5_000_000
            self.progress += 5
            self.stock_price += 2
        elif action == "cut costs":
            self.expenses -= 3_000_000
            self.profits += 2_000_000
            self.stock_price += 1
        elif action == "launch product":
            self.new_products += 1
            self.profits += 10_000_000
            self.stock_price += 5
        elif action == "marketing":
            self.profits -= 2_000_000
            self.progress += 2
            self.stock_price += 3
        # Clamp values
        self.progress = max(0, min(100, self.progress))
        self.stock_price = max(0, self.stock_price)

    def random_action(self):
        return random.choice(["invest", "cut costs", "launch product", "marketing"])

    def show_metrics(self):
        print(f"\n--- {self.name} ---")
        print(f"Progress: {self.progress}%")
        print(f"Profits: ${self.profits:,}")
        print(f"Expenses: ${self.expenses:,}")
        print(f"New Products: {self.new_products}")
        print(f"Stock Price: ${self.stock_price:.2f}")
        print("---------------------\n")

def business_battle():
    user_name = input("Enter your company name: ")
    player = Company(user_name)
    rival = Company("Rival Corp")
    actions = ["invest", "cut costs", "launch product", "marketing"]
    print("Welcome to the Business Battle Game!\n")
    for round in range(1, 6):
        print(f"=== Round {round} ===")
        player.show_metrics()
        rival.show_metrics()
        print("Choose your action:")
        for i, act in enumerate(actions, 1):
            print(f"{i}. {act.title()}")
        choice = input("Enter action number: ")
        try:
            action = actions[int(choice)-1]
        except:
            action = random.choice(actions)
            print(f"Invalid choice. Random action selected: {action}")
        player.take_action(action)
        rival_action = rival.random_action()
        print(f"Rival chooses: {rival_action}")
        rival.take_action(rival_action)
    print("\n=== Final Results ===")
    player.show_metrics()
    rival.show_metrics()
    if player.stock_price > rival.stock_price:
        print(f"Congratulations! {player.name} wins the business battle!")
    elif player.stock_price < rival.stock_price:
        print(f"{rival.name} wins the business battle. Better luck next time!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    business_battle()
