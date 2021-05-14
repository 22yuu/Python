'''
날짜 : 2021/05/14
이름 : 이진유
내용 : 수행 평가 문제 1번

항공사에서는 짐을 부칠 때, 10kg 이상이면 수수료 10,000원을 내야한다. 만약 10kg 미만이면 수수료는 없다.
사용자의 짐의 무게를 키보드로 입력 받아서 사용자가 지불하여야 할 금액을 계산하는 프로그램을 작성하시오.

<출력결과 예시>
짐의 무게는 얼마입니까? 8
수수료는 없습니다.

짐의 무게는 얼마입니까? 15
수수료는 10,000원 입니다.
'''

def fee(weight):
    if weight >= 10:
        return '수수료는 10,000원 입니다.'
    else:
        return '수수료는 없습니다.'

weight = int(input('짐의 무게는 얼마입니까?'))

print(fee(weight))