from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

keyb = ReplyKeyboardMarkup(resize_keyboard=True)
menu_but = KeyboardButton(text='/start')
adm_but = KeyboardButton(text='/admin')
keyb.add(menu_but).add(adm_but)