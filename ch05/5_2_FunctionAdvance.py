'''
날짜 : 2021/04/28
이름 : 이진유
내용 : 파이썬 함수 고급 실습하기 교재 p129
'''

# default 매개변수
def hello(name='홍길동', age=21):
    print('이름 : ', name)
    print('skdl : ', age)
    
hello()
hello('김유신')
hello('김춘추', 31)

# 가변 매개변수 - 매개변수의 값들은 list로 들어감
def total(*nums):
    tot = 0

    for n in nums:
        tot += n

    return tot

r1 = total(1)
r2 = total(1, 2)
r3 = total(1, 2, 3)

print(f'r1 : {r1}')
print(f'r2 : {r2}')
print(f'r3 : {r3}')

# 하나 이상의 리턴값
def sum_and_multi(num1, num2):
    y1 = num1 + num2
    y2 = num1 * num2

    return y1, y2

rs1, rs2 = sum_and_multi(1, 2)
rs3, rs4 = sum_and_multi(3, 4)

print(f'rs1 : {rs1}, rs2 : {rs2}, rs3 : {rs3}, rs4 : {rs4}')

# 변수에 저장하는 함수(익명함수)
def plus(x, y):
    return x+y

def minus(x, y):
    return x-y

var1 = plus

var2 = minus

res1 = var1(1, 2)
res2 = var2(2, 3)

print('res1 : ', res1)
print('res2 : ', res2)

cals = [plus, minus]

res3 = cals[0](3, 4)
res4 = cals[1](4, 5)

print(f'res3 : {res3}')
print(f'res4 : {res4}')


# 람다함수
lam_plus = lambda x, y: x + y

result = lam_plus(2, 3)
print('result : ', result)
