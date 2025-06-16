inventory = {
    "apples": {"quantity": 50, "min_stock": 10},
    "oranges": {"quantity": 30, "min_stock": 15},
    "pears": {"quantity": 20, "min_stock": 10}
}
def add_items(name, quantity, min_stock):
    if name in inventory:
        inventory[name]["quantity"] += quantity
        inventory[name]["min_stock"] = min_stock
        print(f"{quantity} {name} added. Total: {inventory[name]["quantity"]}")
    else:
        inventory[name] = {"quantity": quantity, "min_stock": min_stock}
        print(f"{quantity} {name} added to the inventory")
def search_items(name):
    if name in inventory.keys():
        print(f"there are {inventory[name]["quantity"]} {name} with a minimal stock of {inventory[name]["min_stock"]}")
    else:
        print(f"we do not have any {name}") 
def list_inventory():
    for item, details in inventory.items():
        print(f"{item}: quantity {details["quantity"]} with a minimal stock of {details["min_stock"]}")
def remove_items(name,quantity=1):
    if name in inventory:
        if inventory[name]["quantity"] - quantity >= 0:
            inventory[name]["quantity"] -= quantity
            print(f"{quantity} {name} has been removed")
            if inventory[name]["quantity"] < inventory[name]["min_stock"]:
                print(f"quantity of {name} has dropped below the minimal stock of {inventory[name]["min_stock"]}")                
        else:
            print("quantity cant go below zero")
    else:
        print(f"we do not have any {name}")

add_items("apples",20,10)
add_items("cherries",40,60)
list_inventory()
search_items("cherries")
search_items("bananas")
remove_items("pears")
remove_items("pears",10)
