import random

class BoardMember:
    def __init__(self, name, role, is_user=False):
        self.name = name
        self.role = role
        self.is_user = is_user

    def comment(self, topic, company):
        if self.is_user:
            user_comment = input(f"Your comment on {topic} (as {self.role}): ")
            print(f"{self.name} ({self.role}): {user_comment}")
        else:
            comments = [
                f"I think our {topic} is on track.",
                f"We should focus more on {topic}.",
                f"The {topic} numbers are impressive!",
                f"Let's discuss how to improve {topic}."
            ]
            print(f"{self.name} ({self.role}): {random.choice(comments)}")

    def vote(self, overthrow_plan=False):
        if self.is_user:
            if overthrow_plan:
                user_vote = input("Vote to overthrow the Chairman? (Yes/No/Abstain): ")
            else:
                user_vote = input("Your vote on the proposal? (Yes/No/Abstain): ")
            return user_vote.strip().capitalize()
        else:
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
    user_name = input("Enter your name: ")
    board = [
        BoardMember("Tim Cook", "CEO"),
        BoardMember("Luca Maestri", "CFO"),
        BoardMember("Jeff Williams", "COO"),
        BoardMember("Katherine Adams", "General Counsel"),
        BoardMember("Arthur Levinson", "Chairman"),
        BoardMember(user_name, "Investor", is_user=True)
    ]
    topics = ["progress", "profits", "expenses", "new products", "stock price"]
    print("Welcome to the Apple Board Meeting Simulator!\n")
    for round in range(1, 3):
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

    # Overthrow plan
    print("A secret plan is proposed to overthrow the Chairman (Arthur Levinson)!")
    print("Board votes on the overthrow...")
    overthrow_votes = {member.name: member.vote(overthrow_plan=True) for member in board}
    for name, vote in overthrow_votes.items():
        print(f"{name}: {vote}")
    yes_votes = sum(1 for v in overthrow_votes.values() if v == "Yes")
    if yes_votes > len(board) // 2:
        print("\nThe Chairman has been overthrown! A new era begins at Apple.")
    else:
        print("\nThe overthrow attempt failed. The Chairman remains in power.")
    print("Meeting adjourned. Thank you!")

if __name__ == "__main__":
    run_board_meeting()
