import requests


def reply_to_message(channel_id, message_id, reply_text, api_key):

    data = {
        "content": reply_text,
        "message_reference": {
            "message_id": message_id,
            "channel_id": channel_id,
            "guild_id": None,
        },
    }

    send_message(channel_id, api_key, data)


def send_context_message(channel_id, reply_text, api_key):
    data = {
        "content": reply_text,
    }

    send_message(channel_id, api_key, data)


def send_message(channel_id, api_key, data):
    url = f"https://discord.com/api/v10/channels/{channel_id}/messages"
    headers = {
        "Authorization": api_key,
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            print("Ответ отправлен!")
        else:
            print(f"Ошибка: {response.status_code}\n{response.text}")
    except Exception as e:
        print(f"Произошла ошибка при запросе: {e}")
