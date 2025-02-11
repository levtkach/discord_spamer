import requests
from constants import SYSTEM_PROMT, LM_STUDIO_URL


def generate_text(prompt):

    system_prompt = SYSTEM_PROMT

    data = {
        "model": "deepseek-r1-distill-qwen-7b",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.7,
        "max_tokens": 300,
        "top_p": 0.9,
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
