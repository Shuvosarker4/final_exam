class Restaurant:
    menu = []
    def __init__(self,name):
        self.name = name
    
    def add_item(self,item_name,price):
        self.item_name = item_name
        self.price = price
        item_detail = {'item_name':self.item_name,'price':self.price}
        self.menu.append(item_detail)
        print(f"{item_name} is added\n")

    def remove_item(self,item_name):
        for item in self.menu:
            if(item['item_name'].lower() == item_name.lower()):
                self.menu.remove(item)
                print(f"{item_name} is removed\n")
                break
        else:
            print(f"{item_name} is not found\n")
        
    def view_menu(self):
        print("--- List of all items ---")
        print("Item\tPrice")
        for item in self.menu:
            print(f"{item['item_name']}\t{item['price']}\n")