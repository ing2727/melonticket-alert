import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
from notifier import send_slack, send_email

load_dotenv()

MELON_URL = os.getenv("MELON_URL")
TARGET_DATE = os.getenv("TARGET_DATE")
TARGET_TIME = os.getenv("TARGET_TIME")
TARGET_ZONE = os.getenv("TARGET_ZONE")

def check_ticket():
    try:
        res = requests.get(MELON_URL, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(res.text, "html.parser")

        zone_info = soup.find_all("li", class_="wrap_btn")
        for zone in zone_info:
            text = zone.get_text(strip=True)
            if TARGET_DATE in text and TARGET_TIME in text and TARGET_ZONE in text:
                if "예매가능" in text or "취소표" in text:
                    message = f"🎫 {TARGET_DATE} {TARGET_TIME} / {TARGET_ZONE} 구역에 취소표가 있습니다!\n{MELON_URL}"
                    send_slack(message)
                    send_email("멜론티켓 취소표 알림", message)
                    print(">> 취소표 감지 및 알림 전송")
                    return
        print(">> 취소표 없음")
    except Exception as e:
        print(">> 예외 발생:", e)
