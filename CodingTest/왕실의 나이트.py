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

result += move((row-1)+2, (column-1)+1)
result += move((row-1)+2, (column-1)-1)
result += move((row-1)-2, (column-1)+1)
result += move((row-1)-2, (column-1)-1)

result += move((row-1)+1, (column-1)+2)
result += move((row-1)-1, (column-1)+2)
result += move((row-1)+1, (column-1)-2)
result += move((row-1)-1, (column-1)-2)

print(result)

'''
쌤 풀이
'''

result = 0

# 오른쪽 2칸, 위쪽 1칸
next_row = row + 2
next_col = column - 1

# 오른쪽 2칸, 아래쪽 1칸
next_row = row + 2
next_col = column + 1

# 왼쪽 2칸, 위쪽 1칸
next_row = row - 2
next_col = column - 1

# 왼쪽 2칸, 아래쪽 1칸
next_row = row - 2
next_col = column + 1

# 위쪽 2칸, 오른쪽 1칸
next_row = row + 1
next_col = column - 2

# 위쪽 2칸, 왼쪽 1칸
next_row = row - 1
next_col = column - 2

# 아래쪽 2칸, 오른쪽 1칸
next_row = row + 1
next_col = column + 2

# 아래쪽 2칸 왼쪽 1칸
next_row = row - 1
next_col = column + 2



