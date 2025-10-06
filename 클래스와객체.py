class Student:
    def __init__(self, name, age):
        self.name = name # 인스턴스 변수
        self.age = age # 인스턴스 변수
        
    def greet(self):
        print(f"{self.name}님 안녕하세요!")

student1 = Student("철수", 15)
student2 = Student("영희", 14)

print(student1.name, student1.age) # 학생 이름: 철수, 나이: 15
student1.greet() # 철수님 안녕하세요!
print(student2.name, student2.age) # 학생 이름: 영희, 나이: 14
student2.greet() # 영희님 안녕하세요!