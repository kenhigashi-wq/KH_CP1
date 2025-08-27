import random

class BoardMember:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def comment(self, topic, company):
        comments = [
            f"I think our {topic} is on track.",
            f"We should focus more on {topic}.",
            f"The {topic} numbers are impressive!",
            f"Let's discuss how to improve {topic}."
        ]
        print(f"{self.name} ({self.role}): {random.choice(comments)}")

    def vote(self):
        return random.choice(["Yes", "No", "Abstain"])

class Company:
    def __init__(self, name):
        self.name = name
        self.progress = 70  # out of 100
        self.profits = 100_000_000  # dollars
        self.expenses = 60_000_000  # dollars
        self.new_products = 2
        self.stock_price = 180.0

    def update_metrics(self):
        # Simulate changes
        self.progress += random.randint(-3, 5)
        self.profits += random.randint(-10_000_000, 15_000_000)
        self.expenses += random.randint(-5_000_000, 7_000_000)
        self.new_products += random.choice([0, 1])
        self.stock_price += random.uniform(-5, 7)
        # Clamp values
        self.progress = max(0, min(100, self.progress))
        self.stock_price = max(0, self.stock_price)

    def show_metrics(self):
        print(f"\n--- {self.name} Company Metrics ---")
        print(f"Progress: {self.progress}%")
        print(f"Profits: ${self.profits:,}")
        print(f"Expenses: ${self.expenses:,}")
        print(f"New Products: {self.new_products}")
        print(f"Stock Price: ${self.stock_price:.2f}")
        print("------------------------------\n")

def run_board_meeting():
    company = Company("Apple")
    board = [
        BoardMember("Tim Cook", "CEO"),
        BoardMember("Luca Maestri", "CFO"),
        BoardMember("Jeff Williams", "COO"),
        BoardMember("Katherine Adams", "General Counsel"),
        BoardMember("Arthur Levinson", "Chairman")
    ]
    topics = ["progress", "profits", "expenses", "new products", "stock price"]
    print("Welcome to the Apple Board Meeting Simulator!\n")
    for round in range(1, 4):
        print(f"=== Meeting Round {round} ===")
        company.update_metrics()
        company.show_metrics()
        topic = random.choice(topics)
        print(f"Discussion Topic: {topic.title()}\n")
        for member in board:
            member.comment(topic, company)
        print("\nVoting on new proposal...")
        votes = {member.name: member.vote() for member in board}
        for name, vote in votes.items():
            print(f"{name}: {vote}")
        print("\n--- End of Round ---\n")
    print("Meeting adjourned. Thank you!")

if __name__ == "__main__":
    run_board_meeting()
