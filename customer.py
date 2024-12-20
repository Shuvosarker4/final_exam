from restaurant import Restaurant
class Customer:
    def __init__(self,name,email,phone,balance=0):
        self.name = name
        self.email = email
        self.phone = phone
        self.balance = balance
        self.order = []
    def add_balance(self,amount):
        self.balance += amount
        print(f"{amount} is added\n")

    def view_balance(self):
        print(f"Your balance is {self.balance}\n")
    
    def place_order(self,item_name,quantity):
        self.item_name = item_name
        self.quantity = quantity
        order_detail = {'item_name':self.item_name,'quantity':self.quantity}
        for men in Restaurant.menu:
            if(men['item_name'].lower() == item_name.lower()):
                if(self.balance < quantity*men['price']):
                    print(f"You don't have enough balance.Please add at least {quantity*men['price']} balance\n")
                    self.balance -= quantity*men['price']
                    break
                else:
                    self.order.append(order_detail)
                    print(f"{quantity} {item_name} is successfully delivered\n")
                    break
        else:
            print(f"{item_name} is not found\n")
    
    def view_past_order(self):
        print("--- List of all past orders ---")
        print("Item\tQuantity")
        if(len(self.order) == 0):
            print("No orders found\n")
            return
        else:
            for order in self.order:
                print(f"{order['item_name']}\t{order['quantity']}\n")

