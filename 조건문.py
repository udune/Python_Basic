age = 20
if age >= 18:
    print("성인입니다.")
else:
    print("미성년자입니다.")

password = "1234"
if password == "1234":
    print("로그인 성공")
else:
    print("로그인 실패")

score = 85
if score >= 90:
    print("A학점")
elif score >= 80:
    print("B학점")
elif score >= 70:
    print("C학점")
else:
    print("F학점")

age = 20
is_student = True

if age >= 18:
    if is_student:
        print("성인 학생입니다.")
    else:
        print("성인입니다.")
else:
    if is_student:
        print("미성년자 학생입니다.")
    else:
        print("미성년자입니다.")