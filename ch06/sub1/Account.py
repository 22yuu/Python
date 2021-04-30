# 클래스 정의
class Account:
    # 속성 (__ 캡슐화 private 선언)
    def __init__(self, bank, id, name, money):  # 생성자
        self.__bank = bank  # the name of bank
        self.__id = id  # your account number
        self.__name = name  # your name
        self.__money = money  # your balacne

    # 기능
    def deposit(self, money):
        self.__money += money

    def withdraw(self, money):
        self.__money -= money

    def show(self):
        print('-----------------------------')
        print('은행명 : ', self.__bank)
        print('계좌번호 : ', self.__id)
        print('입금주 : ', self.__name)
        print('현재잔액 : ', self.__money)