import os
import sys

import requests

TOKEN = os.getenv("TELEGRAM_TOKEN")

CHAT_IDS = [
    "-1004231126426",
    "-1004249984029",
    "-1003932802265",
    "-1004476671228",
    "-1003986838980",
]

MESSAGE = """Dziękujemy za dzisiejszy dzień! 💛

Wasza energia, zaangażowanie i każda aktywność naprawdę robią różnicę 💪✨

Przypominamy o aktualizacji aktywności do godziny 20:00 ⏰📲

📝 Formularz aktywności:
👉 https://forms.gle/wBMgLAoHZPyQZezL9

Trzymamy tempo i działamy dalej! 🚀"""

def send_message(chat_id: str) -> bool:
    try:
        response = requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendMessage",
            data={"chat_id": chat_id, "text": MESSAGE},
            timeout=20,
        )
    except requests.RequestException as error:
        # Treść wyjątku może zawierać adres URL z tokenem bota.
        print(f"Błąd połączenia dla {chat_id}: {type(error).__name__}")
        return False

    try:
        payload = response.json()
    except ValueError:
        print(f"Nieprawidłowa odpowiedź Telegram dla {chat_id}: HTTP {response.status_code}")
        return False

    if response.ok and isinstance(payload, dict) and payload.get("ok") is True:
        print(f"Wysłano do {chat_id}")
        return True

    print(f"Błąd wysyłki do {chat_id}: HTTP {response.status_code}")
    return False


def main() -> None:
    if not TOKEN:
        print("Brak zmiennej środowiskowej TELEGRAM_TOKEN")
        sys.exit(1)

    success_count = 0
    for chat_id in CHAT_IDS:
        if send_message(chat_id):
            success_count += 1

    print(f"Wysłano wiadomość do {success_count}/{len(CHAT_IDS)} grup.")
    if success_count != len(CHAT_IDS):
        sys.exit(1)


if __name__ == "__main__":
    main()

