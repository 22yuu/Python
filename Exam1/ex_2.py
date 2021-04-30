'''
날짜 : 2021/04/30
이름 : 이진유
내용 : 파이썬 기본 문제
'''

sum = 0

for k in range(1, 11):
    if k % 2 == 0 or k%3==0:
        sum += k

print('2와 3 배수의 정수의 합 : ', sum)