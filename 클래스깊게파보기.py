class Car:
    def __init__(self, model, color):
        self.model = model # 인스턴스 변수
        self.color = color # 인스턴스 변수
        
myCar = Car("소나타", "흰색")
print(myCar) # 객체 정보 출력
print(myCar.model) # 자동차 모델: 소나타
print(myCar.color) # 자동차 색상: 흰색

class Student:
    def __init__(self, name):
        self.name = name # 인스턴스 변수
        
    def __str__(self):
        return f"Student: {self.name}"

s1 = Student("철수")
print(s1) # Student: 철수

class Point:
    def __init__(self, x, y):
        self.x = x # 인스턴스 변수
        self.y = y # 인스턴스 변수
        
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2
print(p3.x, p3.y) # 6 8