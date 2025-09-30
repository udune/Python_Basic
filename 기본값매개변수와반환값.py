def send_email(to, subject="안내 메일", sender="support@company.com"):
    print(f"{sender} -> {to}: {subject} | 제목: {subject}")
    
send_email("user1", "가입을 환영합니다.", "user2")

def log_event(*messages):
    for msg in messages:
        print(f"LOG: {msg}")

log_event("사용자 로그인", "파일 업로드", "오류 발생")
log_event()  # 아무것도 출력되지 않음
log_event("서버 시작")  # LOG: 서버 시작
