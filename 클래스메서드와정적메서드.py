class Student:
    school_name = "서울고등학교" # 클래스 변수
    
    def __init__(self, name):
        self.name = name # 인스턴스 변수
        
    @classmethod
    def get_school_name(cls):
        return cls.school_name
    
student1 = Student("철수")
student2 = Student("영희")

print(student1.name) # 학생 이름: 철수
print(student2.name) # 학생 이름: 영희
print(Student.get_school_name()) # 서울고등학교
print(student1.get_school_name()) # 서울고등학교
print(student2.get_school_name()) # 서울고등학교
print(Student.school_name) # 서울고등학교
Student.school_name = "부산고등학교" # 클래스 변수 변경

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def is_even(number):
        return number % 2 == 0
    
print(MathUtils.add(3, 5)) # 8
print(MathUtils.is_even(4)) # True
print(MathUtils.is_even(7)) # False
