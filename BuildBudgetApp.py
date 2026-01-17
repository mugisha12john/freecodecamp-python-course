class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
            return True
        return False

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()
    def __str__(self):
        title = self.name.center(30,'*') + '\n'
        items =''
        total = 0
        for item in self.ledger:
             items += f"{item['description'][:23]:23}{item['amount']:7.2f}\n"
             total += item['amount']
        return title + items + f"Total: {total:.2f}"

def create_spend_chart(categories):
    pass

# food = Category('Food')
# food.deposit(1000, 'deposit')
# food.withdraw(10.15, 'groceries')
# food.withdraw(15.89, 'restaurant and more food for dessert')
# clothing = Category('Clothing')
# food.transfer(50, clothing)
# print(food)

def create_spend_chart(categories):
    chart = "Percentage spent by category\n"

    spent = []
    for category in categories:
        total = 0
        for item in category.ledger:
            if item["amount"] < 0:
                total += -item["amount"]
        spent.append(total)

    total_spent = sum(spent)

    percentages = []
    for amount in spent:
        percent = (amount / total_spent) * 100
        percentages.append(int(percent // 10) * 10)

    for level in range(100, -1, -10):
        chart += f"{level:>3}| "
        for percent in percentages:
            if percent >= level:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3) + "\n"

    names = [category.name for category in categories]
    max_length = max(len(name) for name in names)

    for i in range(max_length):
        chart += "     "
        for name in names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        chart += "\n"

    return chart.rstrip("\n")