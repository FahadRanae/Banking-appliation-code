# accounts.py

balance_record = {}   # {customer_id: balance}

def check_balance(customer_id):
    return balance_record.get(customer_id, 0)

def deposit(customer_id, amount):
    balance_record[customer_id] = balance_record.get(customer_id, 0) + amount
    print(f"Deposited {amount}. New Balance: {balance_record[customer_id]}")

def withdraw(customer_id, amount):
    if balance_record.get(customer_id, 0) >= amount:
        balance_record[customer_id] -= amount
        print(f"Withdrawn {amount}. New Balance: {balance_record[customer_id]}")
    else:
        print("Insufficient balance")
