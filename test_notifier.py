# test_notifier.py

from notifier import send_slack, send_email

print("🔔 Slack 테스트 전송...")
send_slack("슬랙 웹훅 테스트 메시지입니다 🎫")

print("📧 이메일 테스트 전송...")
send_email("테스트 메일", "멜론 티켓 알림 시스템 이메일 테스트입니다.")

print("✅ 테스트 완료")
