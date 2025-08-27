# Value is 5, 10, 0, 42
import random
import time

def generate_flash_card():
    operations = ['+', '-', '*', '/']
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    op = random.choice(operations)
    # Avoid division by zero and ensure integer division
    if op == '/':
        num1 = num1 * num2
        question = f"{num1} {op} {num2}"
        answer = num1 // num2
    else:
        question = f"{num1} {op} {num2}"
        answer = eval(question)
    return question, answer

def main():
    print("Flash Card Generator (10 questions per play, type 'q' to quit early)")
    num_questions = 10
    correct = 0
    start_time = time.time()
    for i in range(num_questions):
        question, answer = generate_flash_card()
        print(f"Question {i+1}: {question} = ?")
        user_input = input("Your answer: ")
        if user_input.lower() == 'q':
            break
        try:
            if int(user_input) == answer:
                print("Correct!\n")
                correct += 1
            else:
                print(f"Incorrect. The answer is {answer} you're kinda bad at this\n")
        except ValueError:
            print("Please enter a valid number or 'q' to quit.\n")
    end_time = time.time()
    elapsed = end_time - start_time
    print(f"\nYou got {correct} out of {i+1} correct.")
    print(f"Time taken: {elapsed:.2f} seconds.")

if __name__ == "__main__":
    main()