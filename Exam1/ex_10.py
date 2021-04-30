'''
날짜 : 2021/04/30
이름 : 이진유
내용 : 파이썬 연습문제 이진검색
'''

dataset = [5, 10, 18, 22, 35, 55, 75, 103, 152]
value = int(input('검색할 숫자 입력 : '))

start = 0
end = len(dataset) - 1
loc = 0
state = False

while start <= end:
    mid = (start + end) // 2

    if dataset[mid] > value:
        end = mid - 1
    elif dataset[mid] < value:
        #if(start == mid): break
        start = mid + 1
    else:
        loc = mid
        state = True
        break

# left = 0
# right = len(dataset) - 1
# while left<=right:
#     mid = (left+right)//2
#     if dataset[mid] == value:
#         state = True
#         loc = mid
#         break
#     elif dataset[mid]>value:
#         right = mid-1
#     else :
#         left = mid+1

if state:
    print('찾은 위치 : %d 번째' % (loc + 1))
    print(dataset[mid])
else:
    print('찾는 숫자가 없습니다.')


