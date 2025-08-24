# main.py
import bankcore
import accounts


def main():
    print("Welcome to ABC Bank")
    while True:
        print("\n1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Select option: ")

        if choice == "1":
            name = input("Enter Name: ")
            password = input("Enter Password: ")
            cust_id = bankcore.create_account(name, password)
            accounts.balance_record[cust_id] = 0

        elif choice == "2":
            cust_id = input("Enter Customer ID: ")
            password = input("Enter Password: ")
            if bankcore.login(cust_id, password):
                while True:
                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Logout")
                    ch = input("Select option: ")

                    if ch == "1":
                        amt = float(input("Enter amount: "))
                        accounts.deposit(cust_id, amt)
                    elif ch == "2":
                        amt = float(input("Enter amount: "))
                        accounts.withdraw(cust_id, amt)
                    elif ch == "3":
                        print("Your Balance:", accounts.check_balance(cust_id))
                    elif ch == "4":
                        break
                    else:
                        print("Invalid choice")

        elif choice == "3":
            print("Thank you for using ABC Bank!")
            break

        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
