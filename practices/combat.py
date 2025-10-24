#KH 2nd period, combet practice

import random


def playturn(attrib, monster):
    print("Your turn")
    choice = input("1. Normal Attack\n2.Drink a healing potion (regain 9 health)\n3.Flee (You may or may not get away)\n 4.Pass")
    if choice == "1":
        hit = random.randint(1,20).attrib[2]
        if monster[1]>hit:
            hits = 'You missed!'
        else:
            hits = 'hits'
        print(f"You {hits} with a {hit}")
        if hits == 'hits':
            for i in range(int(attrib[4],[0],[0])):
                dmg += random.randint(1,int(attrib[3][0][2]))
            monster[0] -= dmg
            print("You dealt {dmg} damage.")
                if monster[0]<=0:
                    monster[0] = 0
                    
            return attrib, monster
    elif choice == '3':
        if random.randint(1,20):
            monster[0] = -1
            print("You succesfully escaped!")
        else:
            print("You failed to escape, nerd")


    
print("Welcome to training! First I need to know some things about you!")
name = input("What is your name?:  ")
player = input("What calss fighter are you?\n 1 if you are a Fighter\n 2 if you are a Mage\n 3 if you are a Rouge  ")
print(f"{player}")
print()
if player == "1":
    health = 15
    defense = 10
    attack = ['1d20', 10]
    damage = ['2d6', 5]
elif player == "2":
    health = 10
    defense = 15
    attack = ['1d20', 6]
    damage = ['2d6', 4]
elif player == "3":
    health = 15
    defense = 10
    attack = ['1d20', 6]
    damage = ['2d6', 4]
else:
    print("Invalid input. Try again")
print(f"Your stats are the following.\nHealth: {health},\nDefense: {defense}, \nAttack: {attack,[1]}, \nDamage: {damage,[1]}")