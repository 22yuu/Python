'''
2021/06/03 시각
기출 2019 국가 교육기관 코딩테스트

'''

hour = int(input("분을 입력해주세요."))

count = 0

for h in range(hour+1):
    for m in range(60):
        for s in range(60):
            if s % 10 == 3 or (s % 100) // 10 == 3 or m % 10 == 3 or (m % 100) // 10 == 3 or h % 10 == 3 or (h % 100) // 10 == 3:
                count += 1
                print(f'{h} : {m} : {s}')


print(count)
