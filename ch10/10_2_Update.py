'''
날짜 : 2021/05/20
이름 : 이진유
내용 : 파이썬 데이터베이스 SQL 실습하기
'''

import pymysql

# 데이터베이스 접속
conn = pymysql.connect(host='192.168.10.114',
                       user='22jinuu',
                       password='1234',
                       db='22jinuu',
                       charset='utf8')

# SQL 실행 객체 생성
cur = conn.cursor()

# SQL 실행
sql  = "UPDATE `USER1` SET `hp` = '010-1111-1111' "
sql += "WHERE `uid`='p101';"

cur.execute(sql)
conn.commit()

# 데이터베이스 종료
conn.close()


print("Insert 완료...")

