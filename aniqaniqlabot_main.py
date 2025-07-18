
import logging
import os
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Get token from environment variable
BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("👤 Foydalanuvchi", callback_data="user"),
        InlineKeyboardButton("👥 Guruhlar", callback_data="groups"),
        InlineKeyboardButton("📢 Kanallar", url="https://t.me/pipeto_scalp1"),
        InlineKeyboardButton("📞 Aloqa", url="https://t.me/scalpadminremon")
    )
    await message.answer("👋 Salom! Siz AniQLA botdasiz!

BU BOT SIZGA HAR QANDAY TELEGRAM FOYDALANUVCHILARNI USERNAME ORQALI KIM BILAN MULOQOT QILGAN QAYSI GURUX YOKI KANALGA EGALIGINI KO'RSATIB BERADI", reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data)
async def process_callback(callback_query: types.CallbackQuery):
    if callback_query.data == "user":
        await callback_query.message.answer("👤 Username bo‘yicha foydalanuvchi haqida ma’lumot.")
    elif callback_query.data == "groups":
        await callback_query.message.answer("👥 Guruhlar haqida ma’lumot.")
    await bot.answer_callback_query(callback_query.id)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
