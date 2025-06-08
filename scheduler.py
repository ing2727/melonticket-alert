import schedule
import time
from main import check_ticket

schedule.every(1).minutes.do(check_ticket)

print("🎯 멜론티켓 감시 시작 – 1분 간격으로 확인합니다.")
while True:
    schedule.run_pending()
    time.sleep(1)
