import threading
from collections import defaultdict


class Bank:
    def __init__(self, name, bank_code):
        self.name = name
        self.bank_code = bank_code

    customers = {}

    def add_customer(self, name, customer_id):
        # add if not already exists
        if customer_id not in self.customers:
            self.customers[name] = customer_id
        else:
            raise ValueError("Customer already exists")


class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.accounts = {}

    def add_account(self, account_number, balance=0):
        self.accounts[account_number] = Account(account_number, balance)

    def get_account(self, account_number):
        account = self.accounts.get(account_number, None)
        if account is None:
            raise ValueError("Account not found")
        return account


class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.lock = threading.RLock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount

    def withdraw(self, amount):
        with self.lock:
            if amount > self.balance:
                raise ValueError("Insufficient funds")
            self.balance -= amount


def transfer_funds(from_account: Account, to_account: Account, amount: float):
    accounts_order = sorted([from_account, to_account], key=lambda x: x.account_number)
    with accounts_order[0].lock:
        with accounts_order[1].lock:
            from_account.withdraw(amount)
            to_account.deposit(amount)


if __name__ == "__main__":
    bank = Bank("Hapoalim", 12)
    customer = Customer("Yossi", 123)
    bank.add_customer(customer.name, customer.customer_id)
    print(bank.customers)
    customer.add_account(123, 100.0)
    customer.add_account(456, 200.0)

    transfer_funds(customer.get_account(123), customer.get_account(456), 50.0)
    print(f"Account 123 balance: {customer.get_account(123).balance}")
    print(f"Account 456 balance: {customer.get_account(456).balance}")

    transfer_funds(customer.get_account(123), customer.get_account(456), 150.0)

    print(customer.accounts)
