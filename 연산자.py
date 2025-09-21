a = 10
b = 3
print(a+b)  # 13
print(a-b)  # 7
print(a*b)  # 30
print(a/b)  # 3.3333333333333335
print(a//b) # 3
print(a%b)  # 1
print(a**b) # 1000

x = 5
y = 10
print(x == y) # False
print(x != y) # True
print(x > y)  # False
print(x < y)  # True
print(x >= y) # False
print(x <= y) # True
print(x < 10 and y < 20) # True
print(x < 10 or y > 20) # True
print(x is y) # False
print(x is not y) # True
print(x in [1, 2, 3, 4, 5]) # True
print(y not in [1, 2, 3, 4, 5]) # True

x = 5
x += 3
print(x) # 8
x -= 2
print(x) # 6
x *= 4
print(x) # 24
x /= 3
print(x) # 8.0
x //= 2
print(x) # 4.0
x %= 3
print(x) # 1.0
x **= 4
print(x) # 1.0

letter = "python"
print("p" in letter) # True
print("z" in letter) # False
print("z" not in letter) # True
