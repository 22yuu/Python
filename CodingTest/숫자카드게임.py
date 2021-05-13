'''
날짜 : 2021/05/13
이름 : 이진유
내용 : 숫자 카드 게임 기출 2019 국가 교육기관 코딩 테스트
'''

# n, m, k,를 공백으로 구분하여 입력받기
n, m = map(int, input().split())
 
# 쌤 풀이 
# nums = []
# result = 0
# 
# for i in range(n):
#     data = list(map(int, input().split()))
# 
#     data.sort()
#     num = data[0]
#     nums.append(num)
# 
# nums.sort()
# result = nums[-1]


data = [ 0 for _ in range(n)]
temp = []
answer = 0
for i in range(n):
    data[i] = list(map(int, input().split()))
    data[i].sort()
    temp.append(data[i][0])

temp.sort(reverse=True)

answer = temp[0]

print(answer)





