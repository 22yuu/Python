'''
날짜 : 2021/06/03

코딩테스트 - 왕실의 나이트

'''


def move(x, y):  # x : 수평, y : 수직

    if x < 0 or x >= 8 or y < 0 or y >= 8:
        return 0

    return 1



# 현재 나이트의 위치 입려받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

print(f' row : {row}, column : {column}')

result = 0
map = [[0]*8 for _ in range(8)]


result += move((row-1)+2, (column-1)+1)
result += move((row-1)+2, (column-1)-1)
result += move((row-1)-2, (column-1)+1)
result += move((row-1)-2, (column-1)-1)

result += move((row-1)+1, (column-1)+2)
result += move((row-1)-1, (column-1)+2)
result += move((row-1)+1, (column-1)-2)
result += move((row-1)-1, (column-1)-2)

print(result)



