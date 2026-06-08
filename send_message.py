import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]

CHAT_IDS = [
    "-1004231126426",
    "-1004249984029",
    "-1003932802265"
]

MESSAGE = """Dziękujemy za dzisiejszy dzień! 💛

Wasza energia, zaangażowanie i każda aktywność naprawdę robią różnicę 💪✨

Przypominamy o aktualizacji aktywności do godziny 20:00 ⏰📲

Trzymamy tempo i działamy dalej! 🚀"""

for chat_id in CHAT_IDS:
    response = requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={
            "chat_id": chat_id,
            "text": MESSAGE
        }
    )
    print(chat_id, response.status_code, response.text)
