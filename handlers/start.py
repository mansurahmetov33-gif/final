from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message


from keyboards.inline import maps_keyboard

router = Router()


@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(
        "Welcome to my utility guide bot!\n\n"
        "Choose map:",
        reply_markup = maps_keyboard
    )