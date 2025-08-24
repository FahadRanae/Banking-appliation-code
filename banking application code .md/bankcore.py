# bankcore.py

branch_id = 2057
users_info = {}   # {customer_id: {"name": "abc", "password": "123"}}
user_count = 0

def create_account(name, password):
    global user_count
    user_count += 1
    customer_id = f"{branch_id}-{user_count}"
    users_info[customer_id] = {"name": name, "password": password}
    print(f"Account created successfully! Your Customer ID: {customer_id}")
    return customer_id

def login(customer_id, password):
    if customer_id in users_info and users_info[customer_id]["password"] == password:
        print("Login successful!")
        return True
    else:
        print("Invalid login")
        return False
