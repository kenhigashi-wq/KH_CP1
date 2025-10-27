#KH 2nd period, combet practice

import random


def playTurn(attrib, monster):
    print("Your turn")
    choice = input("1. Normal Attack\n2. Drink a healing potion (regain 9 health)\n3. Flee (You may or may not get away)\n4. any button for Pass")
    if choice == "1":
        hit = random.randint(1,20)+attrib[2]
        if monster[1]>hit:
            hits = 'missed!'
        else:
            hits = 'hits'
        print(f"You {hits} with a {hit}")
        dmg=0
        if hits == 'hits':
            for i in range(int(attrib[3][0][0])):
                dmg += random.randint(1,int(attrib[3][0][2]))
            monster[0] -= dmg
            print(f"You dealt {dmg} damage.")
            if monster[0]<=0:
                monster[0] = 0
                print("You defeated the monster")
        return attrib, monster
    elif choice == '3':
        if random.randint(1,20):
            monster[0] = -1
            print("You succesfully escaped!")
        else:
            print("You failed to escape, nerd")
        return attrib, monster
    elif choice == "2":
        attrib[0]+=9
        print("You regained 9 health!")
        return attrib, monster
    else:
        print("You passed")
        return attrib, monster

def monsterTurn(attrib, monster):
    hit = random.randint(1,50000)+2
    if attrib[1]>hit:
        hits = 'missed! Lucky you'
    else:
        hits = 'hits'
    print(f"The monster {hits} with a {hit}")
    dmg=0
    if hits == 'hits':
        dmg+=random.randint(2,8)+2
        attrib[0] -= dmg
        print(f"You took {dmg} damage.")
        if attrib[0]<=0:
            attrib[0] = 0
            print("You got defeated by the monster! Loser heehawhaw. Nerd")
        else:
            print(f"You have {attrib[0]} health")
    return attrib, monster

print("Welcome to training! First I need to know some things about you!")
name = input("What is your name?:  ")
player = input("What calss fighter are you?\n 1 if you are a Fighter\n 2 if you are a Mage\n 3 if you are a Rouge  ")
print(f"{player}")
print()
if player == "1":
    health = 100
    defense = 20
    attack = 10
    damage = ['2d6', 5]
elif player == "2":
    health = 10
    defense = 15
    attack = 6
    damage = ['2d6', 4]
elif player == "3":
    health = 15
    defense = 10
    attack = 6
    damage = ['2d6', 4]
else:
    print("Invalid input. Try again")
print(f"Your stats are the following.\nHealth: {health},\nDefense: {defense}, \nAttack: {attack,[1]}, \nDamage: {damage,[1]}")
player = [health, defense, attack, damage]
monster = [random.randint(15,20),random.randint(15,20)]

combat = True
if random.randint(1,2) == 1:
    print("You go first")
    turn = True
else:
    print("Monster goes first")
    turn = False
while combat:
    if turn:
        player, monster = playTurn(player, monster)
    else:
        player, monster = monsterTurn(player, monster)
    turn = not turn
    if monster[0]< 1:
        combat = False
        print("You win")
    if player[0]< 1:
        combat = False
        print("You lose, loser nerd, be better, skill issue")
    