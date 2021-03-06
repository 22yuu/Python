'''
날짜 : 2021/04/27
이름 : 이진유
내용 : 파이썬 자료구조 튜플 실습 교재 p92
'''


# Tuple (고정 list) 생성
tuple1 = (1, 2, 3, 4, 5)
print('tuple1 type : ', type(tuple1))
print('tuple1[0] : ', tuple1[0])
print('tuple1[1] : ', tuple1[1])
print('tuple1[2] : ', tuple1[2])

tuple2 = ('서울', '대전', '대구', '부산', '광주')
print('tuple2 type', type(tuple2))
print('tuple2[0] : %s ' % tuple2[0])
print('tuple2[4] : {}'.format(tuple2[4]))

# tuple 수정, 추가, 삭제 X
tuple3 = 1, 2, 3, 4, 5
print('tuple3 type : ', type(tuple3))

# tuple3[1] = 7 # 에러 발생 튜플은 수정 불가
# tuple3[4] = [] # 에러 발생 튜플은 삭제 불가
