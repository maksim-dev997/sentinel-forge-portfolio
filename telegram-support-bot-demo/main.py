from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from config import BOT_TOKEN


dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: types.Message):

    text = (
        "Support Bot\n"
        "\n"
        "Available commands:\n"
        "/faq\n"
        "/contact\n"
        "/admin"
    )

    await message.answer(text)


@dp.message(lambda message: message.text == "/faq")
async def faq_handler(message: types.Message):

    text = (
        "FAQ\n"
        "\n"
        "Q: What does this bot do?\n"
        "A: Customer support.\n"
        "\n"
        "Q: How to contact us?\n"
        "A: Use /contact"
    )

    await message.answer(text)


@dp.message(lambda message: message.text == "/contact")
async def contact_handler(message: types.Message):

    await message.answer(
        "Email: support@example.com"
    )


@dp.message(lambda message: message.text == "/admin")
async def admin_handler(message: types.Message):

    await message.answer(
        "Admin panel placeholder"
    )


async def main():

    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        )
    )

    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
