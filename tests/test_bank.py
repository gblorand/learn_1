import pytest

from bank import Customer, transfer_funds


@pytest.fixture
def bank():
    from bank import Bank
    return Bank("My Bank", "MB")

@pytest.fixture
def customer():
    from bank import Customer
    return Customer("John Doe", "JD")

@pytest.fixture
def account_1():
    from bank import Account
    return Account("1234")


@pytest.fixture
def account_2():
    from bank import Account
    return Account("567")


def test_bank(bank):
    customer = Customer("John Doe", "JD")
    bank.add_customer(customer.name, customer.customer_id)
    customer.add_account(1234, 100)
    customer.add_account(567, 200)
    account_1 = customer.get_account(1234)
    account_2 = customer.get_account(567)
    transfer_funds(account_1, account_2, 50)

    with pytest.raises(ValueError):
        customer.get_account("9999")

    with pytest.raises(ValueError):
        transfer_funds(account_1, account_2, 500)

