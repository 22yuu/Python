'''
날짜 : 2021/04/30
이름 : 이진유
내용 : 파이썬 캡슐화 실습하기 교재 p161

캡슐화 보안을 위해 캡슐화를 진행해야 한다.
'''

from ch06.sub1.Account import Account

kb = Account('국민은행', '101-11-1091', '김유신', 30000)
kb.deposit(10000)
kb.withdraw(5000)
kb.show()

#kb.money -= 1 # 직접 참조