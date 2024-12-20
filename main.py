from admin import Admin
from customer import Customer
from restaurant import Restaurant

def admin_system():
    name = input("Enter Admin Name : ")
    email = input("Enter Admin Email : ")
    phone = input("Enter Admin Phone Number : ")
    admin = Admin(name=name, email=email, phone=phone)
    
    while True:
        print(f"welcome to Admin Panel!!")
        print("1. Create Customer Account")
        print("2. Remove Customer Account")
        print("3. View All Customer")
        print("4. Manage Restaurant Menu")
        print("5. Exit")
        
        choice = int(input("Enter Your Choice : "))

        if(choice == 1):
            name = input("Enter Customer name: ")
            email = input("Enter Customer email: ")
            phone = input("Enter Customer phone number: ")
            admin.add_customer(name=name,email=email,phone=phone)
        elif(choice == 2):
            cus_name = input("Enter customer name: ")
            admin.remove_customer(cus_name)
        elif(choice == 3):
            admin.view_customer()
        elif(choice == 4):
            restaurant_system()
        elif(choice == 5):
            print("Thanks for using our system...")
            break
        else:
            print("Enter valid option")

def restaurant_system():
    
    while True:
        print(f"Welcome to the Restaurant!!")
        print("1. Add Item to Menu")
        print("2. Remove Item from Menu")
        print("3. View Menu")
        print("4. Exit")
        
        choice = int(input("Enter Your Choice: "))

        if(choice == 1):
            item_name = input("Enter Item Name: ")
            price = float(input("Enter Price: "))
            res = Restaurant('KFC')
            res.add_item(item_name,price)
        elif(choice == 2):
            item_name = input("Enter Item Name: ")
            res = Restaurant('KFC')
            res.remove_item(item_name)
        elif(choice == 3):
            res = Restaurant('KFC')
            res.view_menu()
        elif(choice == 4):
            print("Thanks for using our system...")
            break
        else:
            print("Enter valid option")

def customer_system():
    name = input("Enter Your Name : ")
    email = input("Enter Your Email : ")
    phone = input("Enter Your Phone : ")
    cus = Customer(name=name, email=email, phone=phone)
    
    while True:
        print(f"Welcome to Customer {name}!!")
        print("1. View Restaurant Menu")
        print("2. View Balance")
        print("3. Add Balance")
        print("4. Place Order")
        print("5. View Past Orders")
        print("6. Exit")
        
        choice = int(input("Enter Your Choice : "))

        if(choice == 1):
            res = Restaurant('KFC')
            res.view_menu()
        elif(choice == 2):
            cus.view_balance()
        elif(choice == 3):
            amount = float(input("Enter amount to add: "))
            cus.add_balance(amount=amount)
        elif(choice == 4):
            item_name = input("Enter Item Name: ")
            quantity = int(input("Enter Quantity: "))
            cus.place_order(item_name=item_name,quantity=quantity)
        elif(choice == 5):
            cus.view_past_order()
        elif(choice == 6):
            print("Thanks for using our system...")
            break
        else:
            print("Enter valid option")


while True:

    print("--- Restaurant Management System ---")
    print("1. Admin Login")
    print("2. Customer Login")
    print("3. Exit")

    choice = int(input("Select an option: "))
    if(choice == 1):
        admin_system()
    elif(choice == 2):
        customer_system()
    elif(choice == 3):
        print("Thanks for using our system...")
        break
    else:
        print("Enter valid option")