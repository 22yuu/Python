'''
날짜 : 2021/04/29
이름 : 이진유
내용 : 파이썬 내장함수 실습하기 교재 p118
'''

import time

r1 = abs(-5)
print('r1:', r1)



now = time.localtime(time.time())
year = time.strftime('%Y', now)
month = time.strftime('%m', now)
date = time.strftime('%d', now)
hour = time.strftime('%H', now)
min = time.strftime('%M', now)
sec = time.strftime('%s', now)

print('%s년 %s월 %s일')