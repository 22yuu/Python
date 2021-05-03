'''
날짜 : 2021/05/03
이름 : 이진유
내용 : 파이썬 파일입출력 실습 교재 p217
'''

# 파일 읽기

file1 = open('C:/Users/bigdata.DESKTOP-61ML0B4/Desktop/sample.txt')
line = file1.readline()

print('line : ', line)
file1.close()

file2 = open('C:/Users/bigdata.DESKTOP-61ML0B4/Desktop/sample.txt')

while True:
    line = file2.read()
    print('line : ', line)
    if not line:
        break

file2.close()

# 파일 쓰기(File Output)

file3 = open('C:/Users/bigdata.DESKTOP-61ML0B4/Desktop/test.txt', 'w')

file3.write('안녕하세요.\n')
file3.write('반갑습니다.\n')
file3.write('감사합니다.\n')
file3.close()

file4 = open('C:/Users/bigdata.DESKTOP-61ML0B4/Desktop/gugudan.txt', 'w')

for i in range(2,10):
    for j in range(1,10):
        file4.write(f'{i} x {j} = {i*j}\n')

file4.close()