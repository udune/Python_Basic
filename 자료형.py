a = 10
b = 3.5
print(a+b)  # 13.5
print(a-b)  # 6.5
print(a*b)  # 35.0
print(a/b)  # 2.857142857142857
print(a//b) # 2.0
print(a%b)  # 3.0
print(a**b) # 1000.0

name = "Python"
print(name + " 공부")
print(name * 3) # PythonPythonPython
# print(name + 5) # TypeError

is_ready = True
if is_ready:
    print("시작합니다")
else:
    print("준비되지 않았습니다")

x = None
print(x) # None
print(type(x)) # <class 'NoneType'>

age = "25"
print(type(age)) # <class 'str'>
age_num = int(age)
print(type(age_num)) # <class 'int'>
print(age_num) # 25

age = "3"
age_num = float(age)
print(age_num + 10) # 13.0

age = 3
age_str = str(age)
print("나이: " + age_str) # 나이: 3

x = 10
y = "Hello"
print(type(x)) # <class 'int'>
print(type(y)) # <class 'str'>