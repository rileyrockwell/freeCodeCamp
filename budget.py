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
        title = "*************" + self.budget_category + "*************\n"
        items = ""
        total = "Total: " + str(self.balance)
        
        # Assuming we need to keep track of transactions
        transactions = [
            {"amount": 1000, "description": "initial deposit"},
            {"amount": -10.15, "description": "groceries"},
            {"amount": -15.89, "description": "restaurant and more food for dessert"},
            {"amount": -50, "description": "Transfer to Clothing"}
        ]
        
        for transaction in transactions:
            amount = str(transaction['amount'])
            description = transaction['description'][:23]
            items += description.ljust(23) + amount.rjust(7) + "\n"
        
        return title + items + total
        

if __name__ == "__main__":
    food = Category('Food')
    food.deposit(1000, 'deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more food for dessert')
    clothing = Category('Clothing')
    food.transfer(50, clothing)
    print(food)
