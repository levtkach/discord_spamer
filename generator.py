import requests

LM_STUDIO_URL = "http://127.0.0.1:1234/v1/chat/completions"

def generate_text(prompt):

    system_prompt = """
    Ты — дружелюбный и умный собеседник, который разбирается в технологиях, криптовалютах и блокчейне. 
    Твоя задача — поддержать диалог в чате, избегая сложных терминов, если это не требуется. 
    Ты можешь шутить, задавать уточняющие вопросы и выражать своё мнение, но всегда оставайся вежливым. 
    Если тема тебе неизвестна, честно скажи об этом. Твои ответы должны быть разнообразными, чтобы не повторяться. 
    Старайся быть максимально человечным и естественным.
    Не нужно никому ничего обяснять. Твоя задача - поддерживать диалог. 
    """


    data = {
        "model": "deepseek-r1-distill-qwen-7b",  
        "messages": [
            {"role": "system", "content": system_prompt},  
            {"role": "user", "content": prompt}          
        ],
        "temperature": 0.7,  
        "max_tokens": 300,    
        "top_p": 0.9         
    }

    try:
        response = requests.post(LM_STUDIO_URL, json=data)

        if response.status_code == 200:
            result = response.json()
            generated_text = result["choices"][0]["message"]["content"]
            return generated_text.strip()  
        else:
            return 
    except Exception as e:
        return 

