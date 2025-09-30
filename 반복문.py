for i in range(5):
    print("Hello, World!") # 5번 출력

for i in range(5):
    print(i) # 0 1 2 3 4

for ch in "Python":
    print(ch) # 한 글자씩 출력 p y t h o n

count = 0
while count < 5:
    print("반복 중...", count)
    count += 1 # count가 5보다 작을 때까지 반복 0 1 2 3 4

player_hp = 100

while player_hp > 0:
    print("플레이어의 체력:", player_hp)
    player_hp -= 20 # 플레이어의 체력이 0보다 클 때까지 반복 체력 100 80 60 40 20

stock = 5
while stock > 0:
    print("재고가 있습니다. 재고 수량:", stock)
    stock -= 1 # 재고가 있을 때까지 반복 재고 5 4 3 2 1

for i in range(10):
    if i == 5:
        break # i가 5일 때 반복문 종료
    print(i) # 0 1 2 3 4

for i in range(5):
    if i == 2:
        continue # i가 2일 때는 출력하지 않고 다음 반복으로 넘어감
    print(i) # 0 1 3 4