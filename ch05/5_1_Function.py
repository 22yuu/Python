'''
날짜 : 2021/04/28
이름 : 이진유
내용 : 파이썬 함수 실습하기 교재 p114

함수(function)
 - 프로그래밍에서 일련의 로직 단위를 모듈로 만든 것
 - 함수는 정의, 호출로 이루어진다.
'''


# 함수 정의
def f(x):
    y = 2 * x + 3
    return y

# 함수 호출
r1 = f(1)
r2 = f(2)
r3 = f(3)

print(f'r1 : {r1}')
print(f'r2 : {r2}')
print(f'r3 : {r3}')

# 함수유형1 - 매개변수 0, 리턴값 0
def type1(x, y):
    z = x + y
    return z

# 함수유형2 - 매개변수 0, 리턴값 x
def type2(items):
    total = 0

    for item in items:
        total += item

    print('items 합 : ', total)

# 함수유형3 - 매개변수 x, 리턴값 0
def type3():
    total = 0

    for i in range(11):
        total += i

    return total


# 함수유형4 - 매개변수 x, 리턴값 x
def type4():
    print('type3 result : ', type3())

rs1 = type1(1, 2)
rs2 = type1(2, 3)

print('rs1 : ', rs1)
print('rs2 : ', rs2)

type2([1, 2, 3, 4, 5])
type2((2, 4, 6, 8, 10))

result = type3()
print('result : ', result)

type4()

# 확인 문제

def gugudan(dan):
    print(f'{dan} 단')
    for i in range(1, 10):
        print(f'{dan} x {i} = {dan * i}')

gugudan(2)
gugudan(3)
gugudan(7)

