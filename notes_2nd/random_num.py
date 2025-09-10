# KH 2nd random number
import random

# Example of random numbers 
print(random.random()) # Float between 0 and 1
print(random.randint(1, 6))


name = input("what is your name: \n").strip().title()

#Random stat creator
stat_one = random.randint(1,10) + random.randint(1,10)
stat_two = random.randint(1,10) + random.randint(1,10)
stat_three = random.randint(1,10) + random.randint(1,10)
stat_four = random.randint(1,10) + random.randint(1,10)
stat_five = random.randint(1,10) + random.randint(1,10)



print(f"Your stat option: {stat_one}, {stat_two}, {stat_three}, {stat_four}, {stat_five}")
strength = int(input("which stat are you making your strength")) + 2