'''
날짜 : 2021/06/10
이름 : 이진유
내용 : 코딩테스트 - 곱하기 혹은 더하기
'''

str = input()
sum = 0

for i in range(len(str)):

    if sum == 0 :
        sum += int(str[i])
    else:
        if str[i] == '0' or str[i] == '1':
            sum += int(str[i])
        else:
            sum *= int(str[i])
    print(sum)

print(sum)

'''
다른 풀이

data = input()

result = int(data[0])   # 첫 번째 문자를 숫자로 변환해서 대입

for i in range(1, len(data)):

    num = int(data[i])
    
    # num 또는 result가 0 혹은 1인 경우, 곱셈 연산 대신 덧셈 연산을 수행
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)

'''