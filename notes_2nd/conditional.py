# KH 2nd Conditinal Notes

#num = float(input("enter a number: "))

#if num > 0:
    #print(f"The number {num} is positive")
#elif num < 0:
    #print(f"The number {num} is negative")
#else:
    #print(f"The number {num} is a zero")

import random
monster_hp = 30
dmg_modifier = 2
attck_bonus = 3

roll = random.randint(1,20)
number = random.randint(1,20)

if roll == 20:
    print("You succeed!")
    attack = random.randint(1,8) + random.randint(1,8) + dmg_modifier
    monster_hp -+ attack
    print(f"You did {attack} damage to the monster!")
elif roll == 20:
    print("You succeed!")
    attack = random.randint(1,8) + dmg_modifier
    monster_hp -+ attack
    print(f"You did {attack} damage to the monster!")
elif roll <= 10:
    if roll == 1:
        print(f"You rolled a critical failure! The monster gets a free attack")
        damage = random.randint(1,10) + 2
        player_hp -= damage
        print(f"You took {damage} you now have {player_hp} HP")
    else:
        print("YOU MISSED")
else:
    print("That shouldn't be possible")

if False:
    print("I don't know how we got here")
else:
    print("I don't know how we got here")
