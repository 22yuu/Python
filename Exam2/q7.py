'''
날짜 : 2021/05/13
이름 : 이진유
내용 : 파이썬 클래스 상속 연습문제
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print('--------------')
        print('이름', self.name)
        print('나이', self.age)


class Student(Person):
    def __init__(self, name, age, school, major):
        super().__init__(name, age)
        self.school = school
        self.major = major

    def hello(self):
        Person.hello(self)
        print('학교', self.school)
        print('전공', self.major)

class SalaryStudent(Student):
    def __init__(self, name, age, school, major, company):
        super().__init__(name, age, school, major)
        self.company = company

    def hello(self):
        Student.hello(self)
        print('회사', self.company)

if __name__ == '__main__':

    kim = Person('김유신', 24)
    kim.hello()
    
    jang = Student('장보고', 21, '부산대', '영문과')
    jang.hello()

    lee = SalaryStudent('이순신', 31, '부경대', '경영학', '삼성전자')
    lee.hello()

