'''
날짜 : 2021/04/27
이름 : 이진유
내용 : 파이썬 자료구조 셋(set) 실습 교재 p96
'''

# set은 순서가 없고 중복 불가

# set 생성 (집합)
set1 = {1, 2, 3, 4, 5, 3} # 5개 why -> 3 중복
print('set1 type : ', type(set1))
print('set1:',set1)


set2 = set('hello World')
print('set2 type : ', type(set2))
print('set2 : ', set2)

# Set(집합)을 list화 시켜서 값을 추출해서 출력
list1 = list(set1) # set 특성 상 리스트에 들어가 있는 데이터들의 순서는 알 수 없음... 기본적으로 컴파일러 순차적으로 정렬해서 넣어주긴 함
print(list1) # 컴파일러가 순차적으로 정렬해서 넣어주긴 하지만 엄밀히 말하자면 순서를 알 수 없다.

list2 = list(set2)
print('list2 : ', list2)
print('list2[0] : ', list2[0])
print('list2[3] : ', list2[3])




