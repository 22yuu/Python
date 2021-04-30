'''
날짜 : 2021/04/30
이름 : 이진유
내용 : 파이썬 기본 문제
'''

name = input("이름을 입력하시오 : ")
age = input("나이를 입력하시오 : ")

year = 2021 - int(age)

print(f' {name} 님은 {age} 세이고, {year}년도에 태어났습니다.')

n1 = int(input("첫 번째 숫자 입력 : "))
n2 = int(input("두 번째 숫자 입력 : "))
n3 = int(input("세 번째 숫자 입력 : "))

mean = (n1 + n2 + n3) / 3

print(n1, n2, n3, "의 평균은 ", mean, "입니다.")


