'''
날짜 : 2021/06/10
이름 : 이진유
내용 : 코딩테스트 - 문자열뒤집기
'''

str = input()
zero_list = []
one_list = []
cnt_zero = 0
cnt_one  = 0

cnt = 0
for i in range(len(str)):

    if str[i] == '0':
        if cnt_one > 0:
            one_list.append(cnt_one)
            cnt_one = 0
        cnt_zero += 1
    elif str[i] == '1':
        if cnt_zero > 0:
            zero_list.append(cnt_zero)
            cnt_zero = 0
        cnt_one += 1

    if i == (len(str) - 1):
        one_list(cnt_one) if cnt_one > 0 else zero_list.append(cnt_zero)

# print(len(zero_list))
# print(len(one_list))
print(min(len(zero_list), len(one_list)))
