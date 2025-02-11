from time import sleep, time
from random import uniform, randint, choice

from sender import reply_to_message, send_context_message
from parser import get_last_messages
from generator import generate_text
from constants import CHANNEL_ID, MIN_SEC, MAX_SEC, MESSAGE_COUNT, CHAT_URL

last_key = None
while True:
    from constants import CONNECTION_PROFILES

    start_time = time()
    is_reply = bool(randint(0, 1))

    curent_user = choice(
        list(filter(lambda p: p.get("api_key") != last_key, CONNECTION_PROFILES))
    )

    api_key = curent_user.get("api_key")
    user_id = curent_user.get("user_id")
    profile_promt = curent_user.get("profile_promt")

    messages = get_last_messages(CHAT_URL, api_key, MESSAGE_COUNT)

    if not messages:
        continue

    context = "\n".join([message.get("content", "") for message in messages])

    promt = f"""
        Каждое твое сообщение должно быть уникальным. Никогда не повторяй того, что ты писал в прошлом сообщении.
        Тебе нужно сформулировать ответ учитывая контекст сообщений ниже. Будь краток. Ты должен отвечать как человек. 
        Тебе запрещено писать какой-либо текст кроме ответа на сообщение. 
        Никто не должен знать, что ты - нейросеть. Ты - человек, ты общаешься с собеседником. Ты хочешь быть инстересным. Ты не должен повторяться.
        {profile_promt}
        Контекст (последние {MESSAGE_COUNT} сообщений):
        {context}
    """

    message_to_answer = ""
    if is_reply:
        not_curent_users_messages = list(
            filter(lambda m: m.get("author", {}).get("id") != user_id, messages)
        )
        message_to_answer = choice(not_curent_users_messages)
        message_to_answer_text = message_to_answer.get("content")

        promt += f"""
        Сообщение, на которое нужно ответить:
        {message_to_answer_text}
        """

    text = generate_text(promt)
    if is_reply and message_to_answer:
        reply_to_message(CHANNEL_ID, message_to_answer["id"], text, api_key)
    else:
        send_context_message(CHANNEL_ID, text, api_key)

    last_key = api_key
    sleep(uniform(MIN_SEC, MAX_SEC) - (time() - start_time))
