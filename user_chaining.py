class User: 
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):             # first parameter of every method should be "self"
        self.account_balance += amount          ### NB: the "make_deposit" method calls on the User attribute "account_balance" from the "__init__" method. 
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print("User: "+ str(self.name) + ", Balance: "+ str(self.account_balance))
        return self

    def transfer_money(self, amount, User):
        self.account_balance -= amount
        User.account_balance += amount          ### NB: call can be made to the attribute of another User's record, as opposed to "self's"
        return self

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
rian = User("Rian Girard", "rian@python.com")

guido.make_deposit(100).make_deposit(200).make_deposit(700).make_withdrawal(350).display_user_balance()

monty.make_deposit(75).make_deposit(431.73).make_withdrawal(300).make_withdrawal(4.21).display_user_balance()

rian.make_deposit(100000).make_withdrawal(7700).make_withdrawal(12232).make_withdrawal(98.42).display_user_balance()

guido.transfer_money(100, rian).display_user_balance()
rian.display_user_balance()