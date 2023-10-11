import json

def load_inventory(filename):
    file = open(filename)
    inventory = json.load(file)

def save_inventory(filename, inventory):
    with open(filename, 'w') as file:
        json.dump(inventory, file)

inventory_file = "inventory.json"
# load_inventory(inventory_file)
inventory= {}
while True:
    print("Inventory Management System")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. List all items")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        item = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        inventory[item] = inventory.get(item, 0) + quantity
        print(f"{quantity} {item}(s) added to the inventory.")
    elif choice == '2':
        item = input("Enter item name to remove: ")
        if item in inventory:
            quantity = int(input("Enter quantity to remove: "))
            if quantity <= inventory[item]:
                inventory[item] -= quantity
                if inventory[item] == 0:
                    del inventory[item]
                print(f"{quantity} {item}(s) removed from the inventory.")
            else:
                print(f"Insufficient quantity of {item} in inventory.")
        else:
            print(f"{item} not found in inventory.")
    elif choice == '3':
        print("\nInventory:")
        for item, quantity in inventory.items():
            print(f"{item}: {quantity}")
    elif choice == '4':
        save_inventory(inventory_file, inventory)
        print("Inventory data saved. Exiting.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
