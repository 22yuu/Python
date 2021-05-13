'''
날짜 : 2021/05/13
이름 : 이진유
내용 : 큰 수의 법칙 기출 2019 국가 교육기관 코딩 테스트
'''


# n, m, k를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

# n개의 숫자를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort(reverse=True)

# 쌤 풀이 
# first = data[0]
# second = data[1]
# 
# result = 0
# repeat = k
# 
# for i in range(n):
#     
#     if repeat > 0:
#         result += first
#         repeat -= 1
#     else:
#         result += second
#         repeat = k
# 
# print(result)

answer = 0
max = data[0]
idx = 0
cnt = 1

while True:
    #print(f'cnt : {cnt}')
    if cnt == (m+1):
        break

    if (cnt % (k+1)) == 0:
        idx += 1

    if data[idx] >= max:
        answer += data[idx]
        print(data[idx], end=' ')
    else:
        answer += data[idx]
        print(data[idx], end=' ')
        idx = 0

    cnt += 1

print('n : %d, m: %d, k : %d' % (n, m, k))
print('data : ', data)
print(answer)

