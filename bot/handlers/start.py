import io
import os
from asyncio.log import logger
from select import select

from aiogram import types
from aiogram.client import bot
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, InputFile, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, \
    InlineKeyboardMarkup
from dispatcher import dp




def menu_btn():
    k1 = InlineKeyboardButton(text="Dashboard", url="https://megastroy.sector-soft.ru/")
    design = [
        [k1]
    ]
    return InlineKeyboardMarkup(inline_keyboard=design)


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        text=f"Assalomu alaykum <b>{message.from_user.full_name}</b> 😊,"
        "\nPastdagi tugmani tanlang va platformaga ulaning. 🚀",
        reply_markup=menu_btn()
    )