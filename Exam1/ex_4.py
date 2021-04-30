'''
날짜 : 2021/04/30
이름 : 이진유
내용 : 파이썬 기본 문제
'''

for i in range(1, 7):
    for j in range(1, 7):
        tot = i + j

        if tot ==6:
            print('첫번째 주사위 : %d, 두번재 주사위 : %d' % (i, j))