from typing import *

class Category:

    def __init__(self, budget_category):
        self.budget_category = budget_category
        self.balance = 0

    def deposit(self, deposit_amount, description = ''):
        self.balance += deposit_amount
        return self.balance

    def withdraw(self, withdraw_amount, description = ''):
        self.balance -= withdraw_amount
        return self.balance

    def get_balance(self):
        return self.balance

    def transfer(self, amount, transfer_category_instance):
        transfer_category_instance.balance += amount
        self.balance -= amount
        return transfer_category_instance.balance

    def check_funds(self, amount):
        """
        returns False if the amount is greater than the balance
        of the budget category and returns True otherwise
        """
        if amount > self.get_balance():
            return False
        else:
            return True

    def __str__(self):
        print('*************Food*************')
        print('initial deposit\t', self.balance)

        return
        

def create_spend_chart(categories: list):
    "Percentage spent by category"
    pass

        



food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10, 'groceries')
food.withdraw(20, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
# print(food.transfer(50, clothing))
print(food.balance)
print(clothing.balance)
print(food)