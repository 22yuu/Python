'''
날짜 : 2021/04/30
이름 : 이진유
내용 : 파이썬 기본 문제
'''

str = '12345'
sum = 0

for i in range(len(str)):
    num = int(str[i])
    sum += num

print('합 : ', sum)