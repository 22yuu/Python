# 클래스 정의
class Account:
    # 속성
    def __init__(self, bank, id, name, money):  # 생성자
        self.bank = bank  # the name of bank
        self.id = id  # your account number
        self.name = name  # your name
        self.money = money  # your balacne

    # 기능
    def deposit(self, money):
        self.money += money

    def withdraw(self, money):
        self.money -= money

    def show(self):
        print('-----------------------------')
        print('은행명 : ', self.bank)
        print('계좌번호 : ', self.id)
        print('입금주 : ', self.name)
        print('현재잔액 : ', self.money)