class_a = ["철수", "영희", "민수", "철수"]
class_b = ["민수", "수지", "영희"]

a = set(class_a)
b = set(class_b)
c = {"ㅇㅇ", "ㅁㅁ", "ㄴㄴ"}

print(a)  # {'민수', '영희', '철수'}
print(b)  # {'민수', '수지', '영희'}
print(c)  # {'ㅇㅇ', 'ㅁㅁ', 'ㄴㄴ'}

print(c)

students = {"철수", "영희"}
students.add("민수")
print(students)  # {'민수', '철수', '영희'}
students.remove("영희")
print(students)  # {'민수', '철수'}

print(a & b)  # {'민수', '영희'}
print(a | b)  # {'민수', '수지', '영희', '철수'}
print(a - b)  # {'철수'}
print(a ^ b)  # {'철수', '수지'}
print(a.intersection(b))  # {'민수', '영희'}
print(a.union(b))  # {'민수', '수지', '영희', '철수'}
print(a.difference(b))  # {'철수'}
print(a.symmetric_difference(b))  # {'철수', '수지'}
print(a.isdisjoint(c))  # True
print(a.issubset(b))  # False
print(a.issuperset(b))  # False
print(a == b)  # False
print(a != b)  # True

print(len(a))  # 3
print(len(b))  # 3
print(len(c))  # 3
print(len(a & b))  # 2
print(len(a | b))  # 4
print(len(a - b))  # 1
print(len(a ^ b))  # 2
print(len(a.intersection(b)))  # 2
print(len(a.union(b)))  # 4
print(len(a.difference(b)))  # 1
print(len(a.symmetric_difference(b)))  # 2