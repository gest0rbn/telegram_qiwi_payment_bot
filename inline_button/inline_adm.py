from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inl_admin = InlineKeyboardMarkup()
wallet_adm_button = InlineKeyboardButton(text='Список кошельков', callback_data='wallet_list')
inl_admin.add(wallet_adm_button)
