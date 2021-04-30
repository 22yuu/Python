'''
날짜 : 2021/04/30
이름 : 이진유
내용 : 파이썬 상속 실습하기 교재 p165
'''

from ch06.sub2.StockAccount import StockAccount

kb = StockAccount('KB증권', '101-12-1010', '김유신', 10000, '삼성전자', 10, 80000)
kb.deposit(40000)
kb.withdraw(5000)
kb.buy(10, 80000)
kb.sell(10, 80000)
kb.show()


