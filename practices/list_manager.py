# KH 3rd class Shopping List Manager

#Put your shopping list variable here



shop_list = []
print("Press 1, to add item to list. Press 2, to remove an item from list. Press 3, to print shopping list. To break press 4: ")

while True:
    
    action = input("Choose an option (1-4):")
    
    if action == "1":
        item =input("Plese input in item in list: ")
        shop_list.append(item)
        print(f"{item} has been added")
    elif action == "2":
        item = input("Enter item remove: ")
        if item in shop_list:
            shop_list.remove(item)
            print(f"{item} has been removed")
        else:
            print("Item not found")
    elif action == "3":
        if shop_list:
            for i, task in enumerate(shop_list, 1):
                print(f"{i}. {task}")
        else:
            print("list is empty")
    
        
    elif action == "4":
        break
    else:
        print("That shouldn't happen. Try something else")