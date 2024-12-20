class Admin:
    customer =[]
    def __init__(self,name,email,phone):
        self.name = name
        self.email = email
        self.phone = phone

    def add_customer(self,name,email,phone):
        self.name = name
        self.email = email
        self.phone = phone
        customer_detail = {'name':self.name,'email':self.email,'phone':self.phone}
        self.customer.append(customer_detail)
        print(f"{name} is added\n")

    def view_customer(self):
        print("--- List of all customers ---")
        print("Name\tEmail\tPhone")
        # print(f"{self.customer}")
        for cus in self.customer:
              print(f"{cus['name']}\t{cus['email']}\t{cus['phone']}\n")

    def remove_customer(self,customer_name):
        for cus in self.customer:
            if(cus['name'].lower() == customer_name.lower()):
                self.customer.remove(cus)
                print(f"{customer_name} is removed\n")
                break
        else:
            print(f"{customer_name} is not found\n")
    