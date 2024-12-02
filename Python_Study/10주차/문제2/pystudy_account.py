import re

class BankAccount :
    def __init__(self, owner, account_number, balance) :
        self.owner = owner
        self.account_number = account_number
        self.balance = balance
        return
    
    def valid_name(self) :
        check_name = r"^[a-zA-Z]+$"
        check = 0
        if not re.match(check_name, self.owner) :
            print("계좌 소유자 이름의 형식이 올바르지 않습니다.")
            check = 1
        return check
    
    def valid_number(self) :
        check_number = r"^\d{3}-\d{3}$"
        check = 0
        if not re.match(check_number, self.account_number) :
            print("계좌 번호형식이 올바르지 않습니다.")
            check = 1
        return check
    
    def deposit(self, amount) :
        if amount > 0 :
            self.balance += amount
            print("%s 계좌에 %d원 입금 -> 잔액: %d" %(self.owner, amount, self.balance))
        else :
            print("입금 금액이 0이하 입니다.")
        return
    
    def withdraw(self, amount) :
        if (self.balance - amount) >= 0 :
            self.balance -= amount
            print("%s 계좌에서 %d원 출금 -> 잔액: %d" %(self.owner, amount, self.balance))
        else :
            print("잔액이 부족합니다.")
        return
    
    def get_balance(self) :
        return self.balance

class Bank :
    def __init__(self, bank_name) :
        self.bank_name = bank_name
        self.accounts = []
        return
    
    def add_account(self, account) :
        if account.valid_name() == 0 and account.valid_name() == 0 :
            self.accounts.append(account)
            print("- 소유자: %s, 계좌 번호: %s, 잔액: %d" %(account.owner, account.account_number, account.balance))
        else :
            print("이름 or 계좌번호가 올바르지 않습니다.")
        return
    
    def transfer(self, from_account, to_account, amount) :
        for i in self.accounts :
            if i.account_number == from_account :
                fa = i
            else :
                ta = i
        if fa.balance < amount :
            print("잔액이 부족합니다.")
        else :
            fa.balance -= amount
            print("%s에서 %s로 %d원 이체 완료" %(from_account, to_account, amount))
        return
    
# 계좌 생성
account1 = BankAccount("willy", "123-456", 1000)
account2 = BankAccount("spencer", "789-101", 500)

# 유효성 검사
print("=== 계좌 유효성 검사 ===")
if account1.valid_name() == 0 : # 이름 검사
    print("계좌 소유자: %s -> 유효한 이름입니다." %account1.owner)
if account1.valid_number()  == 0 : # 계좌 번호 검사
    print("계좌 번호: %s -> 유효한 계좌 번호입니다.\n" %account1.account_number)

# 은행 객체 생성 및 계좌 추가
bank = Bank("MyBank")
print("=== 계좌 관리 ===")
print("은행 이름: %s" %bank.bank_name)
print("계좌 정보:")
bank.add_account(account1)
bank.add_account(account2)

# 입출금 및 이체
print("\n=== 입출금 및 이체 작업 ===")
account1.deposit(200) # 입금
account2.withdraw(100) # 출금
bank.transfer("123-456", "789-101", 300) # 이체