from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

maps_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mirage", callback_data="map_mirage")
        ],
        [
            InlineKeyboardButton(text="Dust2", callback_data="map_dust2")
        ],
        [
            InlineKeyboardButton(text="Nuke", callback_data="map_nuke")
        ]
    ]
)

mirage_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Utility",
                callback_data="mirage_utility"
            )
        ],
        [
            InlineKeyboardButton(
                text="Solo queue defaults",
                callback_data="mirage_solo_queue"
            )
        ],
        [
            InlineKeyboardButton(
                text="Insta smokes(T side)",
                callback_data="mirage_insta_smokes"
            )
        ],
        [
            InlineKeyboardButton(
                text="Back",
                callback_data="back:maps"
            )
        ]
    ]
)

mirage_utility_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="CT side",
                callback_data="mirage_ct"
            )
        ],
        [
            InlineKeyboardButton(
                text="T side",
                callback_data="mirage_t"
            )
        ],
        [
            InlineKeyboardButton(
                text="Back",
                callback_data="back:mirage"
            )
        ]
    ]
)

mirage_t_side_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Smokes",
                callback_data="mirage_t_smokes"
            )
        ],
        [
            InlineKeyboardButton(
                text="Flashes",
                callback_data="mirage_t_flashes"
            )
        ],
        [
            InlineKeyboardButton(
                text="Molotovs",
                callback_data="mirage_t_molotovs"
            )
        ],
        [
            InlineKeyboardButton(
                text="Back",
                callback_data="back:utility"
            )
        ]
    ]
)

mirage_ct_side_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Smokes",
                callback_data="mirage_ct_smokes"
            )
        ],
        [
            InlineKeyboardButton(
                text="Flashes",
                callback_data="mirage_ct_flashes"
            )
        ],
        [
            InlineKeyboardButton(
                text="Incendiary",
                callback_data="mirage_ct_molotovs"
            )
        ],
        [
            InlineKeyboardButton(
                text="Back",
                callback_data="back:utility"
            )
        ]
    ]
)

mirage_t_smokes_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="A side",
                callback_data="mirage_a_smokes"
            )
        ],
        [
            InlineKeyboardButton(
                text="Mid",
                callback_data="mirage_mid_smokes"
            )
        ],
        [
            InlineKeyboardButton(
                text="B side",
                callback_data="mirage_b_smokes"
            )
        ],
        [
            InlineKeyboardButton(
                text="Back",
                callback_data="back:t_side"
            )
        ]
    ]
)

# mirage_ct_smokes_keyboard = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(
#                 text="A",
#                 callback_data="mirage_a_smokes_ct"
#             )
#         ],
#         [
#             InlineKeyboardButton(
#                 text="B"
#             )
#         ]
#     ]
# )

mirage_a_smokes_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Stairs smoke",
                callback_data="stairs_smoke"
            )
        ],
        [
            InlineKeyboardButton(
                text="Down Stairs Smoke",
                callback_data="down_stairs_smoke"
            )
        ],
        [
            InlineKeyboardButton(
                text="CT smoke",
                callback_data="ct_smoke"
            )
        ],
        [
            InlineKeyboardButton(
                text="Back",
                callback_data="back:t_smokes"
            )
        ]
    ]
)

mirage_mid_smokes_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Connector Smoke",
                callback_data="connector_smoke"
            )
        ],
        [
            InlineKeyboardButton(
                text="Window Smoke",
                callback_data="window_smoke"
            )
        ],
        [
            InlineKeyboardButton(
                text="Start Smoke",
                callback_data="start_smoke"
            )
        ],
        [
            InlineKeyboardButton(
                text="Back",
                callback_data="back:t_smokes"
            )
        ]
    ]
)

mirage_b_smokes_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Short smoke",
                callback_data="short_smoke"
            )
        ],
        [
            InlineKeyboardButton(
                text="Kitchen Smoke",
                callback_data="kitchen_smoke"
            )
        ],
        [
            InlineKeyboardButton(
                text="Main Kitchen smoke",
                callback_data="main_kitchen_smoke"
            )
        ],
        [
            InlineKeyboardButton(
                text="Back",
                callback_data="back:t_smokes"
            )
        ],
        [
            InlineKeyboardButton(
                text="Back",
                callback_data="back:mirage"
            )
        ]
    ]
)

mirage_solo_queue_defaults = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="CT",
                callback_data="mirage_ct_queue"
            )
        ],
        [
            InlineKeyboardButton(
                text="T",
                callback_data="mirage_t_queue"
            )
        ],
        [
            InlineKeyboardButton(
            text="Back",
            callback_data="back:mirage"
            )
        ]
    ]
)


mirage_ct_solo_queue_defaults = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="A",
                callback_data="mirage_ct_queue_a"
            )
        ],
        [
            InlineKeyboardButton(
                text="B",
                callback_data="mirage_ct_queue_b"
            )
        ],
        [
            InlineKeyboardButton(
            text="Back",
            callback_data="back:mirage"
            )
        ]
    ]
)


mirage_t_solo_queue_defaults = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="A",
                callback_data="mirage_t_queue_a"
            )
        ],
        [
            InlineKeyboardButton(
                text="B",
                callback_data="mirage_t_queue_b"
            )
        ]
    ]
)