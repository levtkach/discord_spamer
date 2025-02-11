import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("DISCORD_API_KEY")
LM_STUDIO_URL = "http://127.0.0.1:1234/v1/chat/completions"

url = os.getenv("CHAT_URL")

headers = {
    "Authorization": api_key,  # Токен пользователя или бота
    "Content-Type": "application/json",
    "Referer": "https://discord.com/channels/@me",
    "Sec-Ch-Ua": '"Not?A_Brand";v="99", "Chromium";v="130"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"macOS"',
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 YaBrowser/24.12.0.0 Safari/537.36",
    "X-Debug-Options": "bugReporterEnabled",
    "X-Discord-Locale": "ru",
    "X-Discord-Timezone": "Europe/Volgograd",
}

blockchain_messages = [
    "Привет! Кто-нибудь может объяснить, что такое блокчейн?",
    "Блокчейн — это цепочка блоков, в которых хранятся данные. Каждый блок содержит информацию о предыдущем блоке.",
    "А зачем это нужно?",
    "Это делает систему прозрачной и защищённой от изменений. Например, в криптовалютах это используется для записи транзакций.",
    "Понятно. А как блокчейн связан с майнингом?",
    "Майнинг — это процесс добавления новых блоков в блокчейн. Майнеры решают сложные математические задачи, чтобы подтвердить транзакции.",
    "А какие криптовалюты используют блокчейн?",
    "Почти все! Биткоин, Эфириум, Cardano и многие другие.",
    "А как начать изучать блокчейн? Есть какие-то ресурсы?",
    "Рекомендую начать с книги «Mastering Bitcoin» Андреаса Антонопулоса. Также полезно изучить документацию Ethereum.",
]

def send_message(url, headers, message):
    data = {
        "content": message,
    }
    response = requests.post(url, headers=headers, json=data)
    return response

if 1:
    for message in blockchain_messages:
        response = send_message(url, headers, message)
        if response.status_code == 200:
            print("Сообщение отправлено!")
        else:
            print(f"Ошибка: {response.status_code}")
            print(response.text)

