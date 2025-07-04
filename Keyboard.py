from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

Hello_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Linkni olish")
        ]
    ],
    resize_keyboard=True
)