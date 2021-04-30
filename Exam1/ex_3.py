'''
날짜 : 2021/04/30
이름 : 이진유
내용 : 파이썬 기본 문제
'''

sum = 0

for i in range(1, 11):
    for j in range(1, i+1):
        sum += j
        print('%d' %j, end='+')

    print()

print('총합 : ', sum)