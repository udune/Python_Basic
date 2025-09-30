def greet(name):
    print("안녕하세요", name)
    
greet("철수")  # 안녕하세요 철수
greet("영희")  # 안녕하세요 영희

def add(a, b):
    result = a + b
    return result

result = add(10, 20)
print(result)  # 30

num = len("Python")  # 6
print(num)

def average(a, b, c):
    return (a + b + c) / 3

score = average(90, 80, 70)
print(score)  # 80.0