import requests
from dotenv import load_dotenv
import os

def reply_to_message(channel_id, message_id, reply_text, api_key):
    
    data = {
        "content": reply_text, 
        "message_reference": {
            "message_id": message_id,  
            "channel_id": channel_id,  
            "guild_id": None,          
        },
    }

    send_message(channel_id,api_key, data)


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




# message_to_reply = {'type': 0, 'content': 'привет я бы хотел начать инвестировать', 'mentions': [], 'mention_roles': [], 'attachments': [], 'embeds': [], 'timestamp': '2025-02-11T10:12:43.833000+00:00', 'edited_timestamp': None, 'flags': 0, 'components': [], 'id': '1338814974218211432', 'channel_id': '1338250596050010134', 'author': {'id': '1085249022714974229', 'username': 'bdf2382', 'avatar': '1427c53edb0c7e99a18ff0ba3ea211f4', 'discriminator': '0', 'public_flags': 0, 'flags': 0, 'banner': None, 'accent_color': None, 'global_name': 'Лев Максимович', 'avatar_decoration_data': None, 'banner_color': None, 'clan': None, 'primary_guild': None}, 'pinned': False, 'mention_everyone': False, 'tts': False}

# load_dotenv()
# DISCORD_API_KEY_1 = os.getenv("DISCORD_API_KEY_1")  
# CHANNEL_ID = os.getenv("CHANNEL_ID")   

# # Отправляем ответ
# reply_text = "Блокчейн — это цепочка блоков, в которых хранятся данные. Каждый блок содержит информацию о предыдущем блоке, что делает систему прозрачной и защищённой от изменений."
# # reply_to_message(message_to_reply["channel_id"], message_to_reply["id"], reply_text, DISCORD_API_KEY_1)
# send_context_message(message_to_reply["channel_id"],  reply_text, DISCORD_API_KEY_1)