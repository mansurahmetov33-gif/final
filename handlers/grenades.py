from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.inline import mirage_t_side_keyboard, mirage_ct_side_keyboard, mirage_utility_keyboard, \
    mirage_a_smokes_keyboard, mirage_mid_smokes_keyboard, mirage_b_smokes_keyboard
from keyboards.inline import mirage_utility_keyboard
from keyboards.inline import mirage_t_smokes_keyboard
from aiogram.types import FSInputFile
from aiogram.enums import ChatAction
from data.load_grenades import grenades

from keyboards.inline import (
    mirage_solo_queue_defaults,
    mirage_ct_solo_queue_defaults,
    mirage_t_solo_queue_defaults
)

async def send_grenade_video(
    callback: CallbackQuery,
    grenade
):

    await callback.answer("Loading video...")

    await callback.bot.send_chat_action(
        chat_id=callback.message.chat.id,
        action=ChatAction.UPLOAD_VIDEO
    )

    video = FSInputFile(grenade.path)

    await callback.message.answer_video(
        video=video,
        caption=(
            f"💨 {grenade.title}\n\n"
            f"{grenade.description}"
        )
    )

router = Router()

async def edit_menu(callback, text, keyboard):

    await callback.answer("Loading...")

    await callback.message.edit_text(
        text,
        reply_markup=keyboard
    )

@router.callback_query(F.data == "mirage_utility")
async def mirage_utility(callback: CallbackQuery):
    await callback.answer("Loading...")


    await callback.message.edit_text(
        "Mirage Utility",
    reply_markup = mirage_utility_keyboard
    )



@router.callback_query(F.data == "mirage_solo_queue")
async def mirage_solo_queue(callback: CallbackQuery):
    await callback.answer("Loading...")


    await callback.message.edit_text(
        "Mirage Solo Queue Defaults",
        reply_markup = mirage_solo_queue_defaults
    )

@router.callback_query(F.data == "mirage_ct_queue")
async def mirage_ct_queue(callback: CallbackQuery):
    await callback.message.edit_text(
        "Mirage CT Defaults",
        reply_markup=mirage_ct_solo_queue_defaults
    )

    await callback.answer()

@router.callback_query(F.data == "mirage_t_queue")
async def mirage_t_queue(callback: CallbackQuery):

    await callback.message.edit_text(
        "Mirage T Defaults",
        reply_markup=mirage_t_solo_queue_defaults
    )

    await callback.answer()


@router.callback_query(F.data == "mirage_insta_smokes")
async def mirage_insta_smokes(callback: CallbackQuery):
    await callback.answer("Loading...")


    await callback.message.answer(
        "Mirage Insta Smokes is not done yet"
    )



@router.callback_query(F.data == "mirage_t")
async def mirage_t_side(callback: CallbackQuery):
    await callback.answer("Loading...")


    await callback.message.edit_text(
        "Mirage T Side Utility",
        reply_markup=mirage_t_side_keyboard
    )



@router.callback_query(F.data == "mirage_ct")
async def mirage_ct_side(callback: CallbackQuery):
    await callback.answer("Loading...")

    await callback.message.answer(
        #"Mirage CT Side Utility",
        #reply_markup=mirage_ct_side_keyboard
        "sorry, this one not done yet"
    )






@router.callback_query(F.data == "mirage_t_flashes")
async def mirage_t_flashes(callback: CallbackQuery):
    await callback.answer("Loading...")


    await callback.message.answer(
        #"Mirage Utility",
        #reply_markup=mirage_utility_keyboard
        "sorry flashes not done yet"
    )

@router.callback_query(F.data == "mirage_t_molotovs")
async def mirage_t_molotovs(callback: CallbackQuery):
    await callback.answer("Loading...")


    await callback.message.answer(
        #"Mirage Utility",
        #reply_markup=mirage_utility_keyboard
        "sorry molotovs not done yet"
    )




@router.callback_query(F.data == "mirage_a_smokes")
async def mirage_a_smokes(callback: CallbackQuery):
    await callback.answer("Loading...")


    await callback.message.edit_text(
        "Mirage A site smokes",
        reply_markup = mirage_a_smokes_keyboard
    )



@router.callback_query(F.data == "mirage_mid_smokes")
async def mirage_a_smokes(callback: CallbackQuery):
    await callback.answer("Loading...")


    await callback.message.edit_text(
        "Mirage Mid smokes",
        reply_markup = mirage_mid_smokes_keyboard
    )


@router.callback_query(F.data == "mirage_b_smokes")
async def mirage_a_smokes(callback: CallbackQuery):
    await callback.answer("Loading...")


    await callback.message.edit_text(
        "Mirage B site smokes",
        reply_markup = mirage_b_smokes_keyboard
    )


@router.callback_query(F.data == "mirage_t_smokes")
async def mirage_t_smokes(callback: CallbackQuery):
    await callback.answer("Loading...")


    await callback.message.edit_text(
        "Mirage T Side Smokes",
        reply_markup=mirage_t_smokes_keyboard
    )







@router.callback_query(F.data.in_(grenades.keys()))
async def grenade_handler(callback: CallbackQuery):

    grenade = grenades[callback.data]

    await send_grenade_video(
        callback=callback,
        grenade=grenade
    )


@router.callback_query(F.data.startswith("back:"))
async def universal_back(callback: CallbackQuery):

    back_to = callback.data.split(":")[1]

    keyboards = {
        "utility": mirage_utility_keyboard,
        "t_side": mirage_t_side_keyboard,
        "t_smokes": mirage_t_smokes_keyboard,
        "a_smokes": mirage_a_smokes_keyboard,
        "mid_smokes": mirage_mid_smokes_keyboard,
        "b_smokes": mirage_b_smokes_keyboard,




    }

    texts = {
        "utility": "Mirage Utility",
        "t_side": "Mirage T Side Utility",
        "t_smokes": "Mirage T Side Smokes",
        "a_smokes": "Mirage A Site Smokes",
        "mid_smokes": "Mirage Mid Smokes",
        "b_smokes": "Mirage B Site Smokes"


    }




    await callback.message.edit_text(
        texts[back_to],
        reply_markup=keyboards[back_to]
    )

    await callback.answer()