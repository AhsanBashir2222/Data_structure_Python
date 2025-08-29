from abc import ABC, abstractmethod


class person(ABC):
    def __init__(self, name, userid):
        self.__name = name
        self.__userid = userid

    def set_name(self, name):
        self.__name = name

    def set_id(self, userid):
        self.__userid = userid

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__userid

    @abstractmethod
    def view_detail(self):
        pass


class user(person):
    def __init__(self, name, userid, balance=0):
        super().__init__(name, userid)
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"✅ {amount} deposited successfully")
        else:
            print("❌ Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"✅ {amount} withdrawn successfully")
        else:
            print("❌ Insufficient balance for withdrawal")

    def view_balance(self):
        print(f"💰 Balance: {self.__balance}")

    def view_detail(self):
        print(
            f"👤 User_Id: {self.get_id()} , Name: {self.get_name()} , Balance: {self.__balance}")


class Admin(person):
    def __init__(self, name, adminid):
        super().__init__(name, adminid)
        self.customers = []

    def addcustomer(self, customer):
        if isinstance(customer, user):
            self.customers.append(customer)
            print(f"✅ Customer {customer.get_name()} added successfully")
        else:
            print("❌ Only user type can be added")

    def removecustomer(self, userid):
        for c in self.customers:
            if c.get_id() == userid:
                self.customers.remove(c)
                print(f"✅ Customer {c.get_name()} removed successfully")
                return
        print("❌ Customer not found")

    def view_customer(self):
        print("\n📋 Customer details:")
        if not self.customers:
            print("No customers found.")
        for c in self.customers:
            c.view_detail()

    def view_detail(self):
        print(f"👑 Admin_Id: {self.get_id()} , Name: {self.get_name()}")


# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":

    admin = Admin("Bank Manager", "101")

    while True:
        print("\n===== BANKING MANAGEMENT SYSTEM =====")
        print("1. User Menu")
        print("2. Admin Menu")
        print("3. Exit")
        choice = input("Enter your choice: ")

        # ---------- USER MENU ----------
        if choice == "1":
            if not admin.customers:
                print("❌ No users available. Ask admin to add customers first.")
                continue

            userid = input("Enter your User ID: ")
            current_user = None
            for u in admin.customers:
                if u.get_id() == userid:
                    current_user = u
                    break

            if not current_user:
                print("❌ User not found.")
                continue

            while True:
                print("\n--- USER MENU ---")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. View Balance")
                print("4. View Details")
                print("5. Back to Main Menu")
                u_choice = input("Enter your choice: ")

                if u_choice == "1":
                    amt = float(input("Enter amount to deposit: "))
                    current_user.deposit(amt)

                elif u_choice == "2":
                    amt = float(input("Enter amount to withdraw: "))
                    current_user.withdraw(amt)

                elif u_choice == "3":
                    current_user.view_balance()

                elif u_choice == "4":
                    current_user.view_detail()

                elif u_choice == "5":
                    break

                else:
                    print("❌ Invalid choice")

        # ---------- ADMIN MENU ----------
        elif choice == "2":
            while True:
                print("\n--- ADMIN MENU ---")
                print("1. Add Customer")
                print("2. Remove Customer")
                print("3. View All Customers")
                print("4. View Admin Info")
                print("5. Back to Main Menu")
                a_choice = input("Enter your choice: ")

                if a_choice == "1":
                    name = input("Enter Customer Name: ")
                    uid = input("Enter Customer ID: ")
                    balance = float(input("Enter Initial Balance: "))
                    new_user = user(name, uid, balance)
                    admin.addcustomer(new_user)

                elif a_choice == "2":
                    uid = input("Enter Customer ID to remove: ")
                    admin.removecustomer(uid)

                elif a_choice == "3":
                    admin.view_customer()

                elif a_choice == "4":
                    admin.view_detail()

                elif a_choice == "5":
                    break

                else:
                    print("❌ Invalid choice")

        # ---------- EXIT ----------
        elif choice == "3":
            print("🚪 Exiting... Thank you for using Banking System!")
            break

        else:
            print("❌ Invalid choice. Try again.")
