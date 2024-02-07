class BankAccount:
    def __init__(self, username, password):
        self.balance = 0
        self.username = username
        self.password = password
        self.authenticated = False

    def authenticate(self, input_username, input_password):
        if input_username == self.username and input_password == self.password:
            self.authenticated = True

    def deposit(self, amount):
        if not isinstance(amount, int) or amount <= 0:
            raise Exception("Deposit amount must be a positive integer.")
        if not self.authenticated:
            raise Exception("Authentication required.")
        self.balance += amount

    def withdraw(self, amount):
        if not isinstance(amount, int) or amount <= 0:
            raise Exception("Withdrawal amount must be a positive integer.")
        if not self.authenticated:
            raise Exception("Authentication required.")
        if amount > self.balance:
            raise Exception("Insufficient funds.")
        self.balance -= amount


class MinimumBalanceAccount(BankAccount):
    def __init__(self, username, password, minimum_balance=0):
        super().__init__(username, password)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if amount > self.balance - self.minimum_balance:
            raise Exception("Withdrawal exceeds minimum balance limit.")
        super().withdraw(amount)


class ATM:
    def __init__(self, account_list, try_limit):
        if not isinstance(account_list, list) or not all(
            isinstance(acc, (BankAccount, MinimumBalanceAccount)) for acc in account_list
        ):
            raise Exception("Invalid account list.")
        if not isinstance(try_limit, int) or try_limit <= 0:
            raise Exception("Invalid try limit.")
        self.account_list = account_list
        self.try_limit = try_limit
        self.current_tries = 0

    def show_main_menu(self):
        while True:
            print("1. Log in")
            print("2. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                self.log_in(username, password)
            elif choice == "2":
                break

    def log_in(self, username, password):
        for account in self.account_list:
            account.authenticate(username, password)
            if account.authenticated:
                self.show_account_menu(account)
                return
        self.current_tries += 1
        if self.current_tries == self.try_limit:
            print("Max login attempts reached. Exiting.")
            exit()

    def show_account_menu(self, account):
        while True:
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                amount = int(input("Enter the deposit amount: "))
                account.deposit(amount)
                print(f"Deposited {amount}. New balance: {account.balance}")
            elif choice == "2":
                amount = int(input("Enter the withdrawal amount: "))
                try:
                    account.withdraw(amount)
                    print(f"Withdrew {amount}. New balance: {account.balance}")
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == "3":
                break



account1 = BankAccount("user1", "pass1")
account2 = MinimumBalanceAccount("user2", "pass2", minimum_balance=100)
atm = ATM([account1, account2], try_limit=3)
atm.show_main_menu()
