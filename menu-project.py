import json
class MenuItem:
    def __init__(self,name: str,catagory: str,price: int):
        self.name = name
        self.catagory = catagory
        self.price = price
    
    def __str__(self):
        return f"{self.name}: {self.catagory}, ${self.price}"
    
    def to_dict(self):
        return {"name": self.name, "catagory": self.catagory, "price": self.price}

class MenuManager():
    def __init__(self):
        self.menu = {}

    def add_item(self,item: object):
        if item.catagory not in self.menu:
            self.menu[item.catagory] = {}
        self.menu[item.catagory][item.name] = item
        print(f"Added {item.name} to the {item.catagory} menu")

    def remove_item(self,item: object):
        if item.catagory in self.menu and item.catagory in self.menu[item.catagory]:
            del self.menu[item.catagory][item.name]
            print(f"{item.name} removed from menu")
            if not self.menu[item.catagory]:
                del self.menu[item.catagory]
        else:
            print("Item not found")

    def update_item_price(self,item: object,new_price: int):
        if item.catagory in self.menu and item.name in self.menu[item.catagory]:
            self.menu[item.catagory][item.name].price = new_price
            print(f"updated {item.name} price to {new_price}")

    def list_items_by_catagory(self,catagory):
        if catagory in self.menu:
            for name, items in self.menu[catagory].items():
                print(items)
        else:
            print("items not found")

    def save_to_file(self,filename):
        with open(filename,"w") as f:
            json.dump(self.menu,f,default=to_dict_func,indent=2)
            print("menu saved to file")
    
    def load_from_file(self,filename):
        with open(filename,'r') as f:
            data = json.load(f)
            for catagory, items in data.items():
                if catagory not in self.menu:
                    self.menu[catagory] = {}
                for item_name, item_data in items.items():
                    self.menu[catagory][item_name] = MenuItem(item_name,catagory,item_data['price'])
        print("Menu Loaded From File")
            
def to_dict_func(item):
    return item.to_dict()

coffe = MenuItem("coffe","bevrage",2.50)
latte = MenuItem("latte","bevrage",4.50)
burger = MenuItem("burger","fast-food",5.50)
pizza = MenuItem("pizza","take-out",2.50)
chef = MenuManager()
print(coffe, latte)
chef.add_item(coffe)
chef.add_item(latte)
chef.add_item(burger)
chef.add_item(pizza)
chef.save_to_file("menu_items.json")
chef.load_from_file("menu_items.json")
print(chef.menu)
