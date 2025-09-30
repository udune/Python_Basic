empty_list = []
print(empty_list)  # []

numbers = [1, 2, 3]
print(numbers)  # [1, 2, 3]

mixed = [1, 'a', True]
print(mixed)  # [1, 'a', True]

numbers = [1, 2, 3]
print(len(numbers))  # 3
print(type(numbers))  # <class 'list'>

scores = [90, 85, 70]
print(scores[0])  # 90
print(scores[1])  # 85
print(scores[2])  # 70  
print(scores[-1])  # 70
print(scores[-2])  # 85
print(scores[-3])  # 90

scores.append(100)
print(scores)  # [90, 85, 70, 100]

scores.insert(1, 95)
print(scores)  # [90, 95, 85, 70, 100]

del scores[1]
print(scores)  # [90, 85, 70, 100]

scores.remove(70)
print(scores)  # [90, 85, 100]

scores.pop()
print(scores)  # [90, 85]

scores.clear()
print(scores)  # []

a = [1, 2]
b = [3, 4]
print(a + b)  # [1, 2, 3, 4]
print(a * 3)  # [1, 2, 1, 2, 1, 2]

names = ["철수", "영희", "민수"]
scores = [90, 95, 100]

for i in range(5):
    print(i)  # 0 1 2 3 4

for index, score in enumerate(scores):
    print(index, score)  # 0 90 1 95 2 100

for name, score in zip(names, scores):
    print(name, score)  # 철수 90 영희 95 민수 100
    
numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers if n % 2 == 0]
print(squares)  # [4, 16]
# ==
for number in numbers:
    print(number ** 2)  # 1 4 9 16 25
    
scores = [90, 85, 70, 100]
print(scores[1:3])  # [85, 70]
print(scores[:2])  # [90, 85]

scores = [90, 85, 70, 100]
a,b,c,d = scores
print(a)  # 90
print(b)  # 85
print(c)  # 70
print(d)  # 100

sorted_scores = sorted(scores)
print(sorted_scores)  # [70, 85, 90, 100]
scores.sort()
print(scores)  # [70, 85, 90, 100]

print(85 in scores)  # True
print(95 in scores)  # False

print(scores.index(95))