'''
날짜 : 2021/04/27
이름 : 이진유
내용 : 파이썬 조건문 if 실습 교재 p
'''

# if
num1, num2 = 1, 2

if num1 > 0:
    print('num1은 0보다 크다.')

if num1 > num2:
    print('num1은 num2보다 크다.')

if num1 > 0:
    if num2 > 1:
        print('num1은 0보다 크고 num2는 1보다 크다.')

if num1 > 0 and num2 > 1:
    print('num1은 0보다 크고 num2는 1보다 크다.')


# if ~ else
num3, num4 = 3, 4

if num3 > num4:
    print('num3이 num4보다 크다.')
else:
    print('num3이 num4보다 작다.')


#if ~ elif ~ else
if num1 > num2:
    print('num1은 num2보다 크다.')
elif num2 > num3:
    print('num2은 num3보다 크다.')
elif num3 > num4:
    print('num3응ㄴ num4보다 크다.')
else:
    print('num4가 가장 크다.')

# 삼항 조건문
num = 3

result = num*2 if num >= 5 else num + 2

print(result)

# 확인문제
score = int(input('점수 입력 : '))
print('점수 확인 : ', score)

if score >= 90 and score <= 100:
    print('A 입니다.')
elif score >= 80 and score <= 89:
    print('B입니다.')
elif score >= 70 and score <= 79:
    print('C입니다.')
elif score >= 60 and score <= 69:
   print('D입니다.')
else:
    print('F입니다.')