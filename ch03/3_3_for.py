'''
날짜 : 2021/04/28
이름 : 이진유
내용 : 파이썬 반복문 for 실습
'''

# for
for i in range(5):
    print('i : ', i)


for j in range(10, 20): # 10 ~ 19
    print('j : ', j)

for k in range(10, 0, -1):  # 10 ~ 1
    print('k : ', k)

# 1부터 10까지 합
sum1 = 0

for k in range(11):
    sum1 += k

print('1부터 10까지 합 : ', sum1)

# 1부터 10까지 짝수합
sum2 = 0

for k in range(11):
    if k % 2 == 0:
        sum2 += k

print(f'1부터 10까지 짝수 합 : {sum2}')

# 중첩 for
for a in range(3):

    for b in range(4):
        pass



# 구구단
for dan in range(2, 10):
    print(f'{dan} 단')
    for num in range(1, 10):
        print(f'{dan} x {num} = {dan * num}')

# 별삼각형
for a in range(10,):
    for b in range(a):
        print('☆', end='')
    print()

for a in range(10, 1, -1):
    for b in range(a):
        print('☆', end='')
    print()

for a in range(1, 11):
    for b in range(11-a):
        print('☆', end='')
    print()

for i in range(10):
    print('★' * i)

# List를 이용한 for - I
nums = [1,2,3,4,5]

for num in nums:
    print('num : ', num)

for person in ['김유신','김춘추','장보고']:
    print('persion :', person)


scores = [62, 86, 72, 74, 96]
total = 0

for score in scores:
    total += score
print('score의 총합 : ', total)

# List index value 출력
for index, value in enumerate(scores):
    print('{}, {}'.format(index, value))


# List comprehension
list1 = [1, 2, 3, 4, 5]

list2 = [num*2 for num in list1]
list3 = [num*3 for num in list1 if num % 2 == 1]

print(f'list2 : {list2}')
print(f'list3 : {list3}')

