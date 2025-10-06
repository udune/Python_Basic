class Animal:
    def __init__(self, name):
        self.name = name # 인스턴스 변수
        
    def eat(self):
        print(f"{self.name}가 먹이를 먹습니다.")
        
class Dog(Animal):
    def bark(self):
        print(f"{self.name}가 멍멍 짖습니다.")
        
class Cat(Animal):
    def meow(self):
        print(f"{self.name}가 야옹 야옹 웁니다.")
        
dog = Dog("바둑이")
cat = Cat("나비")

dog.eat() # 바둑이 가 먹이를 먹습니다.
dog.bark() # 바둑이 가 멍멍 짖습니다.
cat.eat() # 나비 가 먹이를 먹습니다.
cat.meow() # 나비 가 야옹 야옹 웁니다.

class Account:
    def __init__(self, owner, balance):
        self.owner = owner # 인스턴스 변수
        self.__balance = balance # 인스턴스 변수
        
    def deposit(self, amount):
        self.__balance += amount
        
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("잔액이 부족합니다.")
            
    def get_balance(self):
        return self.__balance
    
account = Account("철수", 1000) # 계좌 생성
account.deposit(500) # 입금 
print(account.get_balance()) # 1500
account.__balance = 0 # 직접 접근 불가
print(account.get_balance()) # 1500
account.withdraw(2000) # 잔액이 부족합니다.