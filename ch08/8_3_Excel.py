'''
날짜 : 2021/05/03
이름 : 이진유
내용 : 파이썬 외부 패키지 설치 실습 교재 p259
'''

from openpyxl import Workbook

# Excel 파일 쓰기

# 엑셀파일 객체 생성
workbook = Workbook()

# 활성화된 sheet 선택
sheet = workbook.active

# 데이터 입력
sheet['A1'] = '홍길동'
sheet.append([1, 2, 3])
sheet.append(['김유신', '김춘추', '장보고'])
sheet.cell(6, 2, '사과')

# 엑셀파일 저장/닫기
workbook.save('C:/Users/bigdata.DESKTOP-61ML0B4/Desktop/sample.xlsx')
workbook.close()

print('Excel 작업완료....')