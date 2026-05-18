from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.inline import maps_keyboard
from keyboards.inline import mirage_keyboard

router = Router()


@router.callback_query(F.data.startswith("map_"))
async def map_selected(callback: CallbackQuery):

    map_name = callback.data.replace("map_", "")

    if map_name == "mirage":

        await callback.message.edit_text(
            "Mirage Menu",
            reply_markup=mirage_keyboard
        )

    else:

        await callback.message.edit_text(
            f"sorry {map_name} not done yet"
        )

    await callback.answer()

@router.callback_query(F.data == "back:maps")
async def back_maps(callback: CallbackQuery):

    await callback.message.edit_text(
        "Choose a map:",
        reply_markup=maps_keyboard
    )

    await callback.answer()

@router.callback_query(F.data == "back:mirage")
async def back_maps(callback: CallbackQuery):

    await callback.message.edit_text(
        "Mirage menu",
        reply_markup=mirage_keyboard
    )

    await callback.answer()