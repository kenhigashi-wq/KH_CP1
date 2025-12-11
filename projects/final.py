player_health = 1300
player_strength = 200
player_speed = 500
player_charm = .2
player_msp = 0
msp_goal = 500
enemy_stats = {

}

#Inventory (Which is a dictionary)= {weapons: [], charm items: [], heal items: [], speed items: []}
#Make a list for all items
# rooms list = [kitchen, living room, bathroom, garage, Dining room, Hallway, Bedroom, library, Christmas tree room]
#implement a list for visited that is empty(For now)
def charm(enemy_name):
    
def use_item():

def equip_item():

def main_func():#

def start_game():
    print("The eggnog is spiked, the carols are off-key, and a horde of your beloved relatives has breached the perimeter of your house. This isn't a gathering; it's an invasion. \nYou’d hoped for a quiet December, maybe wearing sweatpants and watching bad reality TV. \nInstead, your personal sanctuary has become a war zone of awkward hugs, political arguments, and questionable casserole dishes. \nYour mission, should you choose to accept it, is to defend your turf and maintain your sanity. \nYou need to gather 500 MSP (Mental Stability Points) by successfully navigating conversations, surviving combat encounters, and generally avoiding total psychological collapse. \nYour journey begins in the relative safety of the Foyer. \nThe rest of your pristine home is already overrun. Lock and load your patience. \nMay the odds of a peaceful holiday season be ever in your favor.")
def change_room():

def lose_game():
    if player_health <= 0 and player_msp <= 500:
        print("You got defeated! Your relative moves back in and destroy your peace.")
        print("")
        next = input("Would you like to reattempt to kick your relatives out? yes/no")
        if next == "yes":
            start_game()
        elif next == "no":
            print("You decide you are too tired, you decide to spend christmas with your family, maybe watch a movie or two together.")
def win_game():
    if player_health >= 0 and player_msp >= 500:
        print("You gathered enough MSP! The rest of the of the relatives retreat from your house! You home is peaceful, you now enjoy a cup of hot cocoa and relax")
        print("")
        next = input("Would you like to play again? yes/no")
        if next == "yes":
            start_game()
        elif next == "no":
            print("You decide you had enough fun, you relax with your dog.")
def room():

def combat(enemy_name):
    global player_health, player_strength, player_speed, player_charm, player_msp
    stats = enemystats[enemy_name]
    print(f"{enemy_name}, appears!")

    while player_health > 0 and enemy_health > 0:
        print(f"Your HP:{player_health}|{enemy_name} HP: {enemy_health}")
        action = input("Choose action: attack/charm/heal/exit: ").lower()

        use_item_choice = input("Use an item? yes/no").lower()
        if use_item_choice == "yes":
            use_item()

        if action

