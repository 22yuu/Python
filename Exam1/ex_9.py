'''
날짜 : 2021/04/30
이름 : 이진유
내용 : 파이썬 연습문제 선택정렬
'''

dataset = [3, 5, 1, 2, 4]
size = len(dataset)

for i in range(size - 1):
    for j in range(i+1, size):

        if dataset[i] > dataset[j]:
            tmp = dataset[i]
            dataset[i] = dataset[j]
            dataset[j] = tmp

    print('%d Round : %s' % (i, dataset))

print('Result : ', dataset)