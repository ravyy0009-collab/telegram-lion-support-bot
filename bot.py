import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN not found")

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    @dp.message(CommandStart())
    async def start_handler(message: Message):
        await message.answer(
            "👋 Hello!\n\n"
            "Bot is LIVE ✅\n"
            "Thanks for contacting support 💙"
        )

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
