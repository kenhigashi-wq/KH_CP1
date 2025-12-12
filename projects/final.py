#KH 2nd Final project for SM 1

import random

player = {
    "health": 1300,
    "strength": 200,
    "speed": 500,
    "charm": 0.20,
    "MSP": 0
}

msp_required = 500
defeated = [None]

inventory = {
    "weapons": [],
    "charm items": [],
    "heal items": [],
    "speed items": []
}

rooms = [
    "Kitchen", "Living Room", "Bathroom", "Garage",
    "Dining Room", "Hallway", "Guest Bedroom",
    "Library", "Christmas Tree Room"
]

enemy_names = {
    "Kitchen": "Mom",
    "Living Room": "Dad",
    "Bathroom": "Nieces",
    "Garage": "Uncle",
    "Dining Room": "Aunt",
    "Hallway": "Annoying Cousin",
    "Guest Bedroom": "Grandpa",
    "Library": "Sissy Sister",
    "Christmas Tree Room": "Grandma"
}

enemy_stats = {
    "Uncle": {"dmg": 100, "health": 200, "speed": 300, "MSP": 50},
    "Aunt": {"dmg": 50, "health": 150, "speed": 1000, "MSP": 50},
    "Dad": {"dmg": 200, "health": 250, "speed": 100, "MSP": 50},
    "Mom": {"dmg": 400, "health": 1, "speed": 200, "MSP": 50},
    "Sissy Sister": {"dmg": 100, "health": 300, "speed": 400, "MSP": 50},
    "Annoying Cousin": {"dmg": random.randint(100, 300), "health": 400, "speed": 350, "MSP": 50},
    "Grandpa": {"dmg": 150, "health": 250, "speed": 150, "MSP": 50},
    "Nieces": {"dmg": 50, "health": 100, "speed": 250, "MSP": 50},
    "Grandma": {"dmg": random.randint(200, 500), "health": 500, "speed": 300, "MSP": 300}
}

enemy_attacks = {
    "Uncle": ["You are a dissapointment to this family!", "Wrench Throw!"],
    "Aunt": ["Disgusting casserole!", "Passive Aggressive Strike!", "Makes you change the nieces diaper!"],
    "Dad": ["Dad Yell!", "Grounding Fist!", "Bad Trup impression!"],
    "Mom": ["Mom Rage!", "Chore Attack!", ""],
    "Sissy Sister": ["Door Slam!", "Annoying Mockery!", "Random scream"],
    "Annoying Cousin": ["Nerf Gun Barrage!", "Hyper Tackle!", "Spit on your favorite shirt!", "Bite Attack!"],
    "Grandpa": ["Cane Swipe!", "War Story Strike!"],
    "Nieces": ["Toy Throw!", "High-Pitched Scream!", ""],
    "Grandma": ["Rolling Pin Smash!", "Cookie Shockwave!"]
}

def use_item():
    print("Inventory:", inventory)
    choice = input("Use item or 'no'")
    if choice == "no":
        return
    if choice in inventory["heal items"]:
        player["health"] += 200
        print("+200 HP!")
        inventory["heal items"].pop(choice)
    elif choice in inventory["speed items"]:
        player["speed"] += 100
        print("+100 Speed!")
    elif choice in inventory["charm items"]:
        player["charm"] += 0.05
        print("+5% Charm rate!")
    elif choice in inventory["weapons"]:
        player["strength"] += 100
        print("Player Strength increased by 100!")

def charm(enemy_name):
    print(f"Attempting to charm {enemy_name}...")
    if random.random() < player["charm"]:
        print(f"You succesfully charmed {enemy_name}! They are no longer a threat and leave your house.")
        return True
    else:
        print(f"Charm failed! {enemy_name} is offended!")
        return False
def equip_item():
    
def main_func():
    combat()
def start_game():
    print("The eggnog is spiked, the carols are off-key, and a horde of your oh so beloved relatives has breached the perimeter of your house. This isn't a gathering; it's an invasion. \nYou’d hoped for a quiet December, maybe wearing sweatpants and watching bad reality TV. \nInstead, your personal sanctuary has become a war zone of awkward hugs, political arguments, and questionable casserole dishes. \nYour mission, should you choose to accept it, is to defend your turf and maintain your sanity. \nYou need to gather 500 MSP (Mental Stability Points) by successfully navigating conversations, surviving combat encounters, and generally avoiding total psychological collapse. \nYour journey begins in the relative safety of the Foyer. \nThe rest of your pristine home is already overrun. Lock and load your patience. \nMay the odds of a peaceful holiday season be ever in your favor.")
    main_func()
def change_room():

def lose_game():
    if player["Health"] <= 0 and player["MSP"] <= 500:
        print("You got defeated! Your relative moves back in and destroy your peace.")
        print("")
        next = input("Would you like to reattempt to kick your relatives out? yes/no")
        if next == "yes":
            start_game()
        elif next == "no":
            print("You decide you are too tired, you decide to spend christmas with your family, maybe watch a movie or two together.")
def win_game():
    if player["health"] >= 0 and player["MSP"] >= 500:
        print("You gathered enough MSP! The rest of the of the relatives retreat from your house! You home is peaceful, you now enjoy a cup of hot cocoa and relax")
        print("")
        next = input("Would you like to play again? yes/no")
        if next == "yes":
            start_game()
        elif next == "no":
            print("You decide you had enough fun, you relax with your dog.")
def room():

def combat(enemy_name):
    stats = enemy_stats[enemy_name]
    print(f"{enemy_name}, appears!")

    while player["health"] > 0 and enemy_stats["health"] > 0:
        if enemy_name in defeated:
            print(f"{enemy_name} is already defeated!")
            return True
        stats = enemy_stats[enemy_name]
        hp = stats["health"]
        print(f"Fight {enemy_name}")

        while hp > 0 and player["health"] > 0:
            choice = input("1.Attack 2.Charm 3.Use item 4.Exit")
            use = input("Use item first? yes/no").lower
            if use == "yes":
                use_item
            
            if choice == "1":
                if player["speed"] >= stats["speed"]:
                    hp-= player["strength"]
                    print(f"You hit {enemy_name} for {player['strength']} damage!")
                else:
                    print(f"{enemy_name} was faster than you")
            elif choice == "2":
                if enemy_name == "Grandma":
                    print("Grandma is invincible to your charm!(charm is ineffective)")
                else:
                    if charm(enemy_name):
                        defeated.add(enemy_name)
                        return True
                    else:
                        player["health"] -= stats["dmg"]
                        print(f"{enemy_name} attacks! -{stats['dmg']} HP")
            elif choice == "3":
                use_item()
            elif choice == "4":
                print("Exit Room!")
                return False
            
            if hp <= 0:
                print("You defeated {enemy_name}!")
                defeated.add(enemy_name)
                player["MSP"] += stats["MSP"]
                return True

            attack = random.choice(enemy_attacks[enemy_name])
            print(f"{enemy_name} uses {attack}!")
            player["health"] -= stats["dmg"]
            print(f"Player HP:{player['health']}")