import asyncio
import random
import requests
from telegram.ext import ApplicationBuilder, MessageHandler, filters
from config import AI_BOT_TOKEN, OPENROUTER_API_KEY

API_URL = "https://openrouter.ai/api/v1/chat/completions"

SYSTEM_PROMPT = """
You are a human support agent from Team Goldberg.

Rules:
- Never say you are an AI
- Behave like a real support agent
- Keep replies short
- Ask UID first

Deposit issue → ask payment screenshot
Withdrawal issue → ask withdrawal screenshot
Game issue → ask game screenshot

Language rule:
English → reply English
Hindi → reply Hindi
Hinglish → reply Hinglish
"""

async def ai_reply(update, context):
    user_message = update.message.text
    delay = random.randint(180, 300)
    await asyncio.sleep(delay)

    payload = {
        "model": "z-ai/glm-4.5-air:free",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ]
    }

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(API_URL, json=payload, headers=headers)
    data = response.json()
    reply = data["choices"][0]["message"]["content"]

    await update.message.reply_text(reply)

app = ApplicationBuilder().token(AI_BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), ai_reply))

print("AI Bot Running...")
app.run_polling()