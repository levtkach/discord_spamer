import requests


def get_last_messages(chat_url, api_key, message_count):
    headers = {
        "Authorization": api_key,
        "Content-Type": "application/json",
    }

    url = f"{chat_url}?limit={message_count}"

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            messages = response.json()
            return [
                {
                    k: v
                    for k, v in message.items()
                    if k in ("channel_id", "id", "content", "author")
                }
                for message in messages
            ]
        else:
            print(f"Ошибка: {response.status_code}\n{response.text}")
            return None
    except Exception as e:
        print(f"Произошла ошибка при запросе: {e}")
        return None
