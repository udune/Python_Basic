position = (10, 20)
print(position)  # (10, 20)
print(position[0])  # 10
print(position[1])  # 20

# position[0] = 15  TypeError: 'tuple' object does not support item assignment

colors = ("red", "green", "blue")
print(colors)  # ('red', 'green', 'blue')
print(colors[0])  # 'red'
print(colors[1])  # 'green'
print(colors[2])  # 'blue'

# colors[0] = "yellow"  TypeError: 'tuple' object does not support item assignment

vector2 = (1, 2)
print(vector2)  # (1, 2)
print(vector2[0])  # 1
print(vector2[1])  # 2

# vector2[0] = 3  TypeError: 'tuple' object does not support item assignment

vector3 = (1, 2, 3)
print(vector3)  # (1, 2, 3)
print(vector3[0])  # 1
print(vector3[1])  # 2
print(vector3[2])  # 3

# vector3[0] = 4  TypeError: 'tuple' object does not support item assignment

vector1 = (1,)
print(vector1)  # (1,)
print(vector1[0])  # 1

# vector1[0] = 2  TypeError: 'tuple' object does not support item assignment

tuple1 = (1, 2, 3)
a, b, c = tuple1
new_tuple = list(tuple1)
new_tuple[0] = 4
tuple1 = tuple(new_tuple)
print(tuple1)  # (4, 2, 3)