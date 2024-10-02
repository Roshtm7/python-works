class Bank:
    account_no:int
    account_type:str
    balance:int
    bank_name:str
    
    def create_account(self,account_no,account_type):
        self.account_type="international"
        self.account_no=37623784
        self.balance=3000
        self.bank_name="sbi"

    def deposit(self,amount):
        self.balance+=amount
        print(f"your{self.bank_name}account of{self.account_no}has been credited with{amount}you current balance is{self.balance}")


    def withdrawl(self,amount):
        if amount > self.balance:
            print("insufficient balance")
        else:
            self.balance-=amount
            print(f"you account no{self.account_no}has been debited of amount{amount}now your current balance is{self.balance}")


user_account=Bank()
user_account.create_account(12345,"international")
user_account.deposit(3000)
user_account.withdrawl(1000)

        

