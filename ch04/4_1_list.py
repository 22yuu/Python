'''
날짜 : 2021/04/27
이름 : 이진유
내용 : 파이썬 자료구조 리스트 실습 교재 p844
'''

# 리스트 생성
list1 = [1,2,3,4,5]

print('list type : ', type(list1))
print('list[0] : ', list[0])
print('list[1] : ', list[1])
print('list[2] : ', list[2])


list2 = [5, 3.14, True, 'Apple']

print('list2 type : ', type(list2))
print('list2[1]:', list2[1])
print('list2[2]:', list2[2])
print('list2[3]:', list2[3])

# 리스트 안에 또 다른 리스트가 있는 형태 2차원 배열
list3 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

print('list3 type : ', type(list3))
print('list3[0][0] : ', list3[0][0])
print('list3[1][1] : ', list3[1][1])
print('list3[2][2] : ', list3[2][2])

# list 덧셈
animal1 = ['사자', '호랑이', '코끼리']
animal2 = ['곰', '기린']

result = animal1 + animal2
print('result : ', result)

#list 수정, 추가, 삭제
nums = [1, 2, 3, 4, 5]
print('nums : ', nums)

nums[1] = 7
print('nums :', nums)

nums[2:4] = [8, 9, 10]
print('nums :', nums)

nums[3:5] = []
print('nums :', nums)
