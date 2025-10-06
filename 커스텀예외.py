class NegativeAgeError(Exception):
    """나이가 음수일때 발생하는 예외"""
    pass

def set_age(age):
    if age < 0:
        raise NegativeAgeError("나이는 음수가 될 수 없습니다.")
    print(f"나이가 {age}로 설정되었습니다.")
    
try:
    set_age(-5)
except NegativeAgeError as e:
    print(e)
    
class PasswordTooShortError(Exception):
    def __init__(self, length, min_length=8):
        super().__init__(f"비밀번호가 너무 짧습니다. 최소 {min_length}자 필요. 입력한 길이: {length}")
        self.length = length
        self.min_length = min_length
        
def set_password(pw):
    if len(pw) < 8:
        raise PasswordTooShortError(len(pw))
    
try:
    set_password("abc")
except PasswordTooShortError as e:
    print(e)