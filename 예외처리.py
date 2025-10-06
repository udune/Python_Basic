try:
    num = int(input("숫자를 입력하세요: "))
    print(100 / num)
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except ValueError:
    print("유효한 숫자를 입력하세요.")
    
try:
    f = open("data.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
finally:
    f.close()